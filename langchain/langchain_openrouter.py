from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from os import getenv
from dotenv import load_dotenv

load_dotenv()

template = """Question: {question}
Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm = ChatOpenAI(
  api_key=getenv("OPENROUTER_API_KEY"),
  base_url=getenv("OPENROUTER_BASE_URL"),
  model="openai/gpt-5-chat",
  max_tokens=3000,
  temperature=0.7,
 # default_headers={
  #  "HTTP-Referer": getenv("YOUR_SITE_URL"),
  #  "X-Title": getenv("YOUR_SITE_NAME"),
  #}
)

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "what is langchain and its use in agentic ai development?"

print(llm_chain.run(question))
