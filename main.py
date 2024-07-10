import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain.prompts import ChatPromptTemplate

load_dotenv()


template_msg = "Ton role est de repondre a des question {question}, les questions vont se baser sur des context {context}"
system_msg_prompt = SystemMessagePromptTemplate.from_template(template_msg)

human_msg_prompt = HumanMessagePromptTemplate.from_template(
                                input_vars = ["question", "context"],
                                template = "{question}",
                                )

chat_prompt_template = ChatPromptTemplate.from_messages([system_msg_prompt, human_msg_prompt])


question = "What is LangChain?"
context = "User guide"
res = chat_prompt_template.format_messages(question=question,context=context)

print(res)