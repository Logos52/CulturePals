import os
#from dotenv import load_dotenv
from os import getenv

print(os.environ.get('TELEGRAM_API_TOKEN'))
print("test 1")

print(getenv('TELEGRAM_API_TOKEN'))
