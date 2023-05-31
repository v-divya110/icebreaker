from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

def main(information):
    load_dotenv()
    
    summary_template = """Given the LinkedIn information {information} about a person I want you to create
    1. a short summary
    2. two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    print(chain.run(information=information))
    
def get_data_from_linkedin(url):
    information = scrape_linkedin_profile(url, call_api=True)
    return information
 

if __name__ == "__main__":
    # main()
    linkedin_url = linkedin_lookup_agent(name="Eden Marco")
    information = get_data_from_linkedin(linkedin_url)
    main(information)