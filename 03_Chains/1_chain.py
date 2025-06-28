from set_key import set_openai_key

set_openai_key()
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

llm = OpenAI(temperature=0.6)

shop_name_prompt_temp = PromptTemplate(input_variable=['comodity'],
                                       template="suggest 1 good name for shop which sells {comodity} ")


shop_name_chain = LLMChain(llm=llm, prompt=shop_name_prompt_temp)
ans = shop_name_chain.run("Leather boots")
print(f"Ans for shop name = {ans}")
