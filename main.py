import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI


def main():
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if not api_key:
        raise RuntimeError("Enviroment variable wasnt found")

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()


    messages = [
        {"role": "user", "content": args.user_prompt},
    ]

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
    )

    if response.usage is None:
        raise RuntimeError("The usage property is None. Likely failed API request.")

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
        #print("Response: \n" + response.choices[0].message.content)
    else:
        print("Response: \n" + response.choices[0].message.content)


if __name__ == "__main__":
    main()
