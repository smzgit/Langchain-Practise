from set_key import set_openai_key

set_openai_key()
from langchain_openai import OpenAI

llm = OpenAI(temperature=0.6)
names = llm(prompt="suggest some good names for shop which sells diamonds & it's jeweleries ")
print(names)
