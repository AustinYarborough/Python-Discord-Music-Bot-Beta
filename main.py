from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message

# step 0 load our discord token from somewhere safe
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
print(TOKEN)