from set_key import set_openai_key

set_openai_key()

from langchain.chains import SimpleSequentialChain

from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.chains import LLMChain

llm = OpenAI(temperature=0.6)

shop_name_prompt_temp = PromptTemplate(input_variable=['comodity'],
                                       template="suggest 1 good name for shop which sells {comodity} ")

shop_name_chain = LLMChain(llm=llm, prompt=shop_name_prompt_temp)

items_prompt_temp = PromptTemplate(input_variable=['shop'],
                                   template="Suggest 5-8 items I can sells in {shop} ")

items_chain = LLMChain(llm=llm, prompt=items_prompt_temp)
seq_chain = SimpleSequentialChain(chains=[shop_name_chain, items_chain])
ans = seq_chain.run("Goldfish")
print(f"items are:\n {ans}")
