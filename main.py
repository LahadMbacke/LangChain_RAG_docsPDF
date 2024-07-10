import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
model = ChatOpenAI()

template_msg = "Ton role est de repondre a des question {question}, les questions vont se baser sur des context {context}"
system_msg_prompt = SystemMessagePromptTemplate.from_template(template_msg)

human_msg_prompt = HumanMessagePromptTemplate.from_template(
                                input_vars = ["question", "context"],
                                template = "{question}",
                                )

chat_prompt_template = ChatPromptTemplate.from_messages([system_msg_prompt, human_msg_prompt])


def load_doc(docs):
    
    loaders = PyPDFLoader(docs)
    pages = loaders.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 600, chunk_overlap = 50)
    doc_split = text_splitter.split_documents(pages)
    return doc_split

def load_embeddings(doc_sp):
    embed = OpenAIEmbeddings()
    db = Chroma.from_documents(doc_sp,embed)
    return db.as_retriever()


def test(docs):
    doc_cunks = load_doc(docs)
    retriever = load_embeddings(doc_cunks)
    vectors = retriever.get_vectors()
    
    for vec in vectors:
        print(vec)


