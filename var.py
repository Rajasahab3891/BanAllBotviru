import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list

class Var:
    API_ID = int(os.getenv("API_ID", "28196711"))
    API_HASH = os.getenv("API_HASH", "a8a23bffb12aae7a4c72fa2b4cd538a1")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7068063178:AAHPqyvvIqiWFFeMIa-A5koNkOMiL-s9BAw")
    sudo = os.getenv("6655939309, 7738551811, 6472500481")
    SUDO = []
    if sudo:
        SUDO = make_int(sudo)
