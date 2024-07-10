import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema import StrOutputParser
import streamlit as st
import tempfile


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


st.header("<h1> RAG simple <h1>")


# file = "CPRO.pdf"
def load_doc(file):
    
    loaders = PyPDFLoader(file)
    pages = loaders.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 600, chunk_overlap = 50)
    doc_split = text_splitter.split_documents(pages)
    # st.write(doc_split)
    return doc_split
upload_file = st.file_uploader("Choose youy file",type="pdf")

def upload(upload_file):
    if upload_file is not None:
        with tempfile.NamedTemporaryFile(delete=False,suffix="pdf") as tem_file:
            tem_file.write(upload_file.read())
            tem_file_path = tem_file.name
        try:
            st.write("Document chargé avec succès!")
            return load_doc(tem_file_path)

        except Exception as e:
            st.error(f"Erreur lors du chargement du fichier PDF: {e}")
        finally:
            os.remove(tem_file_path)





def load_embeddings(doc_sp):
    embed = OpenAIEmbeddings()
    db = Chroma.from_documents(doc_sp,embed)
    return db.as_retriever()


def response(retriever,query):
    chain = (
        {"context":retriever,"question": RunnablePassthrough()}
        | chat_prompt_template
        | model
        | StrOutputParser()
    )
    return chain.invoke(query)
   


doc_cunks = upload(upload_file)
retriever = load_embeddings(doc_cunks)
# query = "Quelles sont les aides financières pour l’employeur ?"   

st.title("RAG")
if "messages" not in st.session_state:
    st.session_state.messages =[]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
# React to user input
query = st.chat_input("Posez votre question ici :")
if query :
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(query)

    # Add user message to chat history
    st.session_state.messages.append({"role":"user","content":query})


with st.chat_message("assisatant"):
    answer = response(retriever,query)
    st.markdown(answer)
st.session_state.messages.append({"role":"assistant","content":answer})



