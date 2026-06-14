
from models import Product

genai.configure(
    api_key="upload api key"
)

model = genai.GenerativeModel("gemini-1.5-flash")

def process_message(message):

    products = Product.query.all()

    product_list = "\n".join([
        f"{p.name} | ₹{p.price} | {p.description}"
        for p in products
    ])

    prompt = f"""
You are ShopBot, an AI shopping assistant.

Available Products:
{product_list}

Your tasks:
- Recommend products from the available products list.
- Explain the project when asked.
- Answer in the same language as the user.
- Keep answers concise and friendly.

User Message:
{message}
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"