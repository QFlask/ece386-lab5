'''Passes a personal intro statement to an LLM.
The LLM produces valid JSON that could be ingested into a database to create a new user.

Modified from https://ollama.com/blog/structured-outputs
'''
from ollama import chat
from pydantic import BaseModel
import sys

class User(BaseModel):
  name: str
  age: int | None
  job: str | None
  hobbies: str | None
 
class UserList(BaseModel):
  users: list[User]

def get_users(prompt: str) -> UserList:
    response = chat(
    messages=[
        {
        'role': 'user',
        'content': prompt
        }
    ],
    model='llama3.1',
    format=User
    )
    
    users = UserList.model_validate_json(response.message.content)

    return users

def main():
    # verify system arguments
    if len(sys.argv) != 2:
        print("Usage: python user_creation.py \"prompt\"")
        exit(1)

    prompt: str = sys.argv[1]
    print(f"Creating users from the prompt: \n{prompt}")

    users = get_users(prompt)
    
    print(f"Users created:\n{users}")

if __name__ == "__main__":
   main()
