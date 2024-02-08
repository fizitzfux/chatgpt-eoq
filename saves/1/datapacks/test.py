import time

# Function to read Minecraft server log for chat messages
def read_minecraft_log():
    with open('/home/sven/openai-eoq/logs/latest.log', 'r') as log_file:
        log_file.seek(0, 2)  # Move cursor to end of file
        while True:
            new_line = log_file.readline()
            if new_line:
                if '[Server thread/INFO]' in new_line and '<' in new_line:
                    # Extract chat message from log line
                    chat_message = new_line.split('> ')[-1].strip()
                    # send_to_chatgpt(chat_message)
                    print(chat_message)
            else:
                time.sleep(1)  # Sleep for 1 second before checking for new lines

# Function to send chat message to ChatGPT API
def send_to_chatgpt(message):
    # Send message to ChatGPT API and process response
    # Implement this part based on the API documentation
    pass

# Main function
def main():
    read_minecraft_log()

if __name__ == "__main__":
    main()