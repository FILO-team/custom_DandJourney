import re

from .config import BOT_TOKEN, SERVER_ID, VIP_TOKEN, CHANNEL_ID, \
                    USE_MESSAGED_CHANNEL, MID_JOURNEY_ID, AGENT_CHANNEL, \
                    HAS_RUN, BOT_NAME, PROXY_URL, PROXY_AUTH
# 권한 목록 기능 소개，나중에 단계적으로 폐지될 예정이다.，데이터베이스 레코드로 변경
from .config import AUTHORITY_LIST

from .parameter import Banned_Word, DjPromptDic, DBlendPromptDic, DDescribePromptDic


def ConfigCheck(Config):
    if bool(re.findall("^_Add.*HERE_$", Config)):
        raise ValueError("초기 변수{}정의되지 않음".format(Config))
    return Config


BotSettings = {
    "BotCode" : {
        "BOT_TOKEN": ConfigCheck(BOT_TOKEN),
        "SERVER_ID": ConfigCheck(SERVER_ID),
        "VIP_TOKEN": ConfigCheck(VIP_TOKEN),
        "CHANNEL_ID": ConfigCheck(CHANNEL_ID),
        "MID_JOURNEY_ID": MID_JOURNEY_ID,
    },
    "BotOpt" : {
        "USE_CHANNEL": USE_MESSAGED_CHANNEL,
        "AGENT_SIGN": bool(AGENT_CHANNEL),
        "AGENT_CHANNEL": AGENT_CHANNEL,
        "PROXY_URL": PROXY_URL,
        "PROXY_AUTH": PROXY_AUTH,
        "HAS_RUN": HAS_RUN
    },
    "BotInfo" : {
        "Name": BOT_NAME,
        "version": "v2.0.1",
    },
    "BotInit" : {
        "Speed": "Fast",
    },
    "BotParam" : {
        "Banned_Word" : Banned_Word,
        "DJPrompt" : DjPromptDic,
        "DBlendPrompt" : DBlendPromptDic,
        "DDescribePrompt" : DDescribePromptDic,
    },
}

