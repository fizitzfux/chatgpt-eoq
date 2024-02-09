from openai import OpenAI
import time
import io

# Function to read Minecraft server log for chat messages
def read_minecraft_log():
    with io.open('./logs/latest.log','r', buffering=1) as log_file:
        log_file.seek(0, 2)  # Move cursor to end of file
        while True:
            new_line = log_file.readline()
            if new_line:
                if '[Server thread/INFO]' in new_line and '<' in new_line:
                    # Extract chat message from log line
                    chat_message = new_line.split('> ')[-1].strip()
                    send_to_chatgpt(chat_message)
                    print(chat_message)
            else:
                time.sleep(1)  # Sleep for 1 second before checking for new lines

# Function to send chat message to ChatGPT API
def send_to_chatgpt(message):
    # Send message to ChatGPT API and process response
    # Implement this part based on the API documentation
    openai = OpenAI(
        api_key="qhr3cy383obm", base_url="https://openai.sd42.nl/api/providers/openai/v1"
    )

    prompt = message

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Minecraft 1.20.4 if asked for give then use the /give command and @p"},
            {"role": "user", "content": prompt},
        ],
    )

    output = response.choices[0].message.content

    print(output)

    # Check credit status
    print(openai.models.with_raw_response.list().headers["OpenAiProxy"])

# Main function
def main():
    read_minecraft_log()

if __name__ == "__main__":
    main()

