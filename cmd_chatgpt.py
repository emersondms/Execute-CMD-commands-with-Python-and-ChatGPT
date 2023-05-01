import openai
import subprocess

openai.api_key = "your-api-key"

def generate_cmd_command(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Write a Windows cmd command that: {text}",
        temperature=0.7,
        max_tokens=2048,
        n=1,
        stop=None
    )
    return response['choices'][0]['text'].strip()

def execute_cmd_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True)
        print(f"Result: {result}")
    except subprocess.CalledProcessError as ex:
        print(ex)

command_description = input("Type the command description: ")
command = generate_cmd_command(command_description)
print(f"Command generated: {command}")
execute_cmd_command(command)
