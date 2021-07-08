import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import SUDO, BIO_MESSAGE, API_ID, API_HASH, HANDLER, BOT_TOKEN
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
abcd = API_ID
efgh = API_HASH
ijkl = BOT_TOKEN
SUDO = []
for x in SUDO:
  SUDO.append(x)
  
