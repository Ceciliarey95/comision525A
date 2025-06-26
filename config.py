from dotenv import load_dotenv
import os

load_dotenv()

USER_DB = os.getenv("USER_DB")
PASS_DB = os.getenv("PASS_DB")
HOST_DB = os.getenv("HOST_DB")