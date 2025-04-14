'''Passes a personal intro statement to an LLM.
The LLM produces valid JSON that could be ingested into a database to create a new user.

Modified from https://ollama.com/blog/structured-outputs
'''
from ollama import chat
from pydantic import BaseModel
import sys
from typing import Optional

class User(BaseModel):
  name: Optional[str] = None
  age: Optional[int] = None
  job: Optional[str] = None
  hobbies: Optional[str] = None
 
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
    model='gemma3:1b',
    format=User.model_json_schema()
    )

    print(response.message.content)
    
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
