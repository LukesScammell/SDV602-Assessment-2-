import os

MONGO_URI = os.environ["SDV602_MONGO_URI"]

DB_NAME = "sdv602_des"
DATA_SOURCES_COLLECTION = "data_sources"
CHAT_MESSAGES_COLLECTION = "chat_messages"
USER_COLLECTION = "users"

POLL_RATE = 1000