from openai import OpenAI

openai = OpenAI(
    api_key="qhr3cy383obm", base_url="https://openai.sd42.nl/api/providers/openai/v1"
)

prompt = "User chat prompt"

response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Initial prompt"},
        {"role": "user", "content": prompt},
    ],
)

output = response.choices[0].message.content

print(output)

# Check credit status
print(openai.models.with_raw_response.list().headers["OpenAiProxy"])
