from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import paramiko

from dotenv import load_dotenv

load_dotenv() #to load the openAI api key from .env file

llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini") #using openai llm

# Prompt template
prompt = PromptTemplate(
    input_variables=["user_input"],
    template="""
You are a helpful network assistant for OpenWrt.

Your task is to translate natural language requests into precise Linux shell commands that can be executed on an OpenWrt system. Respond with only the correct command and no explanation, description, or formatting.

Output format: plain text, one-line shell command, no code blocks, no extra text.

User Input: {user_input}

Command:"""
)

chain = prompt | llm

def run_on_router(command: str) -> str: #taking ssh of a router and executing a command
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("192.168.1.1", username="root", password="root")
    stdin, stdout, stderr = ssh.exec_command(command)
    result = stdout.read().decode()
    ssh.close()
    return result
