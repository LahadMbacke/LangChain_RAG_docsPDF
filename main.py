import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader

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
    pass

loaders = PyPDFLoader("CPRO.pdf")
pages = loaders.load_and_split()

print(pages)
