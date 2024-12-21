# template_python_fastapi_repo/examples/simple-openai-chat.py

from openai import OpenAI
from template_python_fastapi_repo.settings import Settings
from template_python_fastapi_repo.helpers.logger_helper import get_logger

# Get the configured logger
logger = get_logger()

settings = Settings()

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def get_chat_response(messages):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
        )
        # Accessing the content attribute directly
        chat_content = response.choices[0].message.content

        # Extracting token usage details
        token_usage = response.usage

        return chat_content, token_usage
    except Exception as e:
        logger.error(f"Error during OpenAI API call: {e}")
        return "Sorry, I couldn't process your request.", None


# Initialize conversation memory
conversation_memory = []


# ANSI escape codes for colors and styles
class Colors:
    BOLD = "\033[1m"  # Bold
    USER = "\033[94m"  # Blue
    ASSISTANT = "\033[92m"  # Green
    RESET = "\033[0m"  # Reset to default color
    ITALIC = "\033[3m"  # Italic
    END_ITALIC = "\033[23m"  # End Italic


# Example interactive loop
while True:
    user_input = input(
        f"{Colors.BOLD}{Colors.USER}You: {Colors.RESET}"
    )  # Bold user label
    if user_input.lower() in ["exit", "quit"]:
        break

    # Add user message to conversation memory
    conversation_memory.append({"role": "user", "content": user_input})

    # Get response from the model
    chat_response, token_usage = get_chat_response(conversation_memory)

    # Add assistant message to conversation memory
    conversation_memory.append({"role": "assistant", "content": chat_response})

    # Optionally, print the response and token usage to the console
    if token_usage:
        print(
            f"\n------\n{Colors.ITALIC}*Token Usage: {token_usage}*{Colors.END_ITALIC}\n------\n"
        )  # Print token usage in italics
    print(
        f"{Colors.BOLD}{Colors.ASSISTANT}ChatGPT: {Colors.RESET}{chat_response}\n"
    )  # Bold assistant label
