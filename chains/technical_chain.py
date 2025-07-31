from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

tech_prompt = PromptTemplate(
    input_variables=["user_query", "user_email"],
    template="""
You are an EdTech system that drafts emails for technical issues.

User issue: {user_query}
Student email: {user_email}

Generate a professional email to the Technical Support Team describing the issue.
CC the student in the email. Just output the email content, not subject.
    """
)

def generate_tech_email(user_query: str, user_email: str):
    final_prompt = tech_prompt.format(user_query=user_query, user_email=user_email)
    return llm.invoke(final_prompt).content.strip()
