from langchain_core.runnables import RunnableLambda
from chains.faq_chains import get_faq_answer
from chains.technical_chain import generate_tech_email
from chains.billing_chain import generate_billing_email

# 1️⃣ Identify the Route
def classify_query(user_query: str) -> str:
    """
    Return one of: FAQ, TECH, BILLING
    """
    user_query_lower = user_query.lower()
    
    # Step 1: Check FAQ first
    faq_answer = get_faq_answer(user_query)
    if faq_answer != "NO_MATCH":
        return "FAQ"

    # Step 2: Keyword-based routing for simplicity
    if any(word in user_query_lower for word in ["error", "bug", "not working", "login failed", "technical"]):
        return "TECH"
    if any(word in user_query_lower for word in ["payment", "refund", "invoice", "billing", "money"]):
        return "BILLING"

    return "FAQ"  # Default to FAQ if nothing matches

# 2️⃣ Define RunnableRouter
def handle_user_query(user_query: str, user_email: str):
    route = classify_query(user_query)

    if route == "FAQ":
        answer = get_faq_answer(user_query)
        return f"FAQ Response: {answer}"

    elif route == "TECH":
        email_content = generate_tech_email(user_query, user_email)
        return f"Technical Issue Email Draft:\n\n{email_content}"

    elif route == "BILLING":
        email_content = generate_billing_email(user_query, user_email)
        return f"Billing Issue Email Draft:\n\n{email_content}"

# 3️⃣ Quick Test
if __name__ == "__main__":
    queries = [
        ("I forgot my password", "student1@example.com"),
        ("My payment is not reflecting", "student2@example.com"),
        ("The website is not working for me", "student3@example.com"),
        ("Do you provide job placement?", "student4@example.com")
    ]

    for q, email in queries:
        print("Query:", q)
        print(handle_user_query(q, email))
        print("-" * 80)
