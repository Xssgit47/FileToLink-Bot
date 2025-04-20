from os import environ as env
from dotenv import load_dotenv

load_dotenv()

class Telegram:
    API_ID = int(env.get("23418117"))
    API_HASH = str(env.get("e93479e4b3eae090bf90a978b14ffc09"))
    BOT_TOKEN = str(env.get("7690173014:AAFBSxUmB-sB05HhNYUrA7_uOs97IFCLqjE"))
    OWNER_ID = int(env.get('OWNER_ID', '7506224965'))
    WORKERS = int(env.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    DATABASE_URL = str(env.get('mongodb+srv://viraaj35:viraajmongo@danger35.wgk98.mongodb.net/?retryWrites=true&w=majority&appName=Danger35'))
    UPDATES_CHANNEL = str(env.get('https://t.me/FN7DANGER', "Telegram"))
    SESSION_NAME = str(env.get('DANGER-ZONE', 'FileStream'))
    FORCE_SUB_ID = env.get('@FN7DANGER', None)
    FORCE_SUB = env.get('@FN7DANGER', False)
    FORCE_SUB = True if str(FORCE_SUB).lower() == "true" else False
    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "60"))
    FILE_PIC = env.get('FILE_PIC', "https://graph.org/file/5bb9935be0229adf98b73.jpg")
    START_PIC = env.get('START_PIC', "https://graph.org/file/290af25276fa34fa8f0aa.jpg")
    VERIFY_PIC = env.get('VERIFY_PIC', "https://graph.org/file/736e21cc0efa4d8c2a0e4.jpg")
    MULTI_CLIENT = False
    FLOG_CHANNEL = int(env.get("-1002197681899", None))   # Logs channel for file logs
    ULOG_CHANNEL = int(env.get("-1002197681899", None))   # Logs channel for user logs
    MODE = env.get("MODE", "primary")
    SECONDARY = True if MODE.lower() == "secondary" else False
    AUTH_USERS = list(set(int(x) for x in str(env.get("AUTH_USERS", "")).split()))

class Server:
    PORT = int(env.get("PORT", 8080))
    BIND_ADDRESS = str(env.get("BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(env.get("PING_INTERVAL", "1200"))
    HAS_SSL = str(env.get("HAS_SSL", "0").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(env.get("NO_PORT", "0").lower()) in ("1", "true", "t", "yes", "y")
    FQDN = str(env.get("FQDN", BIND_ADDRESS))
    URL = "http{}://{}{}/".format(
        "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
    )



