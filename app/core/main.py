
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="xai-P5pcZrC3P8ggJyH3y1z6BFxofFQz2tVU2S90p3nKnzR9KoQw02qdZReM1dNJwIL9xZERFdTzynIYXNcJ"  # Replace with your actual API key
)

try:
    # Make the API call
    completion = client.chat.completions.create(
        model="x-ai/grok-vision-beta",  # Adjust the model if needed
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What is your name "
                    },

                ]
            }
        ]
    )

    # Print the entire response
    print("API Response:", completion)

except Exception as e:
    print(f"An error occurred: {e}")
