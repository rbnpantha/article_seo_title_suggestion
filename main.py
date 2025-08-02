import os
from openai import OpenAI
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Sample article (replace or load from file)
article_text = """
Apple unveiled the iPhone 15 at its annual September event, featuring a new titanium frame, USB-C charging port, and improved camera capabilities. The company also introduced the Apple Watch Series 9, boasting a new S9 chip that enables double-tap gestures and on-device Siri processing.

The iPhone 15 Pro models include a 3nm A17 Pro chip, making them more powerful and efficient. Apple emphasized environmental sustainability, announcing its first carbon-neutral products and eliminating leather from all accessories.

Pre-orders for the iPhone 15 series begin this Friday, with availability starting next week. Prices start at $799 for the base model.
"""

# Prompt to generate titles and SEO tags
prompt = f"""
You are an expert SEO strategist and news editor. Read the article below and generate:
1. Five catchy and informative title suggestions.
2. Ten SEO-friendly tags (keywords) that would help this article rank better.

Article:
\"\"\"
{article_text}
\"\"\"
"""

# Generate response
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.7
)

# Print and save result
result = response.choices[0].message.content
print(result)

# Optionally save to file
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(result)
