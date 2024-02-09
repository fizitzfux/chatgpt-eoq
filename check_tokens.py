from openai import OpenAI


openai = OpenAI(
    api_key="qhr3cy383obm", base_url="https://openai.sd42.nl/api/providers/openai/v1"
)

# Check credit status
print(openai.models.with_raw_response.list().headers["OpenAiProxy"])
