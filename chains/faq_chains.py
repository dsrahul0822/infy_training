from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from utils.faq_loader import load_faq_data

from dotenv import load_dotenv
load_dotenv()


# Load FAQ JSON
faq_list = load_faq_data()

# Create a FAQ text for prompt
faq_text = "\n".join([f"Q: {faq['question']}\nA: {faq['answer']}" for faq in faq_list])

# Initialize LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Prompt Template for FAQ
prompt = PromptTemplate(
    input_variables=["user_query", "faq_data"],
    template="""
You are an EdTech FAQ assistant.

Here is a list of FAQs with answers:
{faq_data}

User question: {user_query}

Task:
1. If the question matches or is similar to any FAQ, respond with the correct answer.
2. If no FAQ is relevant, respond with: "NO_MATCH"
    """
)

def get_faq_answer(user_query: str):
    # Format the prompt
    final_prompt = prompt.format(user_query=user_query, faq_data=faq_text)

    # Call LLM
    response = llm.invoke(final_prompt)

    return response.content.strip()
