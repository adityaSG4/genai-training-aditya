import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

questions = [
    "What is the capital of Maharashtra?",
    "Who wrote the Ramayana?",
    "What are the annual charges of the Platinum Sapphire Credit Card from SuryaFirst Bank?",
    "What are the current RBI repo rate and today's date?",
    "What is the customer-care number of SuryaFirst Bank?",
]

# for question in questions:
#     response = client.chat.completions.create(
#         model="openai/gpt-oss-20b:free",
#         messages=[
#             {
#                 "role": "user",
#                 "content": question,
#             }
#         ],
#     )

#     answer = response.choices[0].message.content

#     print("\n" + "=" * 70)
#     print("Question:", question)
#     print("Answer:", answer)


SYSTEM_PROMPT = """
If you are not certain or the information may be out of date,
say "I don't know" instead of guessing.
"""

for question in questions:
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": question,
            },
        ],
    )

    answer = response.choices[0].message.content

    print("\n" + "=" * 70)
    print("Question:", question)
    print("Answer:", answer)