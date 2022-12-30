import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    TG_BOT_TOKEN = "5989527178:AAGE13kpv859YYecSJr_wSL3oARV0I9DFUM"
    APP_ID = "17718356"
    API_HASH = "fe2dec8e960bf8dcb4e4820d81fe7d46"
    TG_USER_SESSION = "BQCf3ZJRphYVxJOGlvDIY29BPwTKR9RKYxJgJX_gNqDLZPA80z_9R1qOuA1aTbDxU7RomZXwDh4_6SC6fux7PGn_mLsVjX-m6xuV3uXPK4r4XRNVwvpv9O8RnDyMMWr8UsXX8dO5T3MgepIPa0RZCQRQ94KccoobX_VEjv2hzgeQ3t-skRwZZLTTJpa-NFN3_mrfLNcB8IA7HTMNi4nlzT5Ljbom-dtlHbQoM9Bau3ozyW16DgCYhrss3DwERrWoi022YK_0iOqpvLn0mBEwr3Eox9oinZHbLIk792XOyMX5lkh9526C1JIj-SdayRkpvtRzXNYpFoFWAMkqWTjxUHk0AAAAAVre2SwA"
    DB_URI = "mongodb+srv://amritsinghbaba01:1998@cluster0.3tacgfj.mongodb.net/?retryWrites=true&w=majority"

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
