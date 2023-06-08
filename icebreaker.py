from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parser import person_intel_parser

load_dotenv()

def main(information):
    result = None
    if information:
        summary_template = """Given the LinkedIn information {information} about a person I want you to create
        1. a short summary
        2. two interesting facts about them
        3. 2 creative ice breakers to open a conversation with them
        \n{format_instructions}
        """
        summary_prompt_template = PromptTemplate(
            input_variables=["information"], 
            partial_variables={"format_instructions": person_intel_parser.get_format_instructions()},
            template=summary_template
        )
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        chain = LLMChain(llm=llm, prompt=summary_prompt_template)
        result = chain.run(information=information)
    return result


def get_data_from_linkedin(url):
    information = scrape_linkedin_profile(url, call_api=True)
    return information


def ice_break(name: str) -> str:
    linkedin_url = linkedin_lookup_agent(name=name)
    print(linkedin_url)
    information = get_data_from_linkedin(linkedin_url)
    return main(information)


if __name__ == "__main__":
    result = ice_break(name="Eden Marco")
    print("Result", result)
