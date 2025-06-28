from langchain_core.prompts import PromptTemplate

shop_name_prompt_temp = PromptTemplate(input_variable=['comodity'],
                                  template="suggest 1 good name for shop which sells {comodity} ")

print(shop_name_prompt_temp.format_prompt(comodity="gold & silver"))