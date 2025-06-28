import os
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.chains import LLMChain

os.environ["OPENAI_API_KEY"] =""

llm = OpenAI(temperature=0.6)
# names = llm(prompt="suggest some good names for shop which sells diamonds & it's jeweleries ")
# print(names)

shop_name_prompt_temp = PromptTemplate(input_variable=['comodity'],
                                  template="suggest 1 good name for shop which sells {comodity} ")

# print(prompt_temp_name.format_prompt(comodity="gold & silver"))

shop_name_chain = LLMChain(llm=llm,prompt=shop_name_prompt_temp)
# ans=chain.run("Leather boots")
# print(ans)

items_prompt_temp = PromptTemplate(input_variable=['shop'],
                                  template="Suggest 5-8 items I can sells in {shop} ")

from langchain.chains import SimpleSequentialChain
items_chain = LLMChain(llm=llm,prompt=items_prompt_temp)
seq_chain = SimpleSequentialChain(chains=[shop_name_chain, items_chain])
ans=seq_chain.run("Goldfish")
print(f"items are:\n {ans}")