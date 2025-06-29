from openai import OpenAI

client = OpenAI(api_key="your-api-key")

def assess_risk(data):
    chat_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a cybersecurity expert."},
            {"role": "user", "content": f"Analyze this Shodan result: {data}"}
        ]
    )
    return chat_response.choices[0].message.content
