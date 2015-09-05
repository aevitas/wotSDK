# Embedded file name: scripts/common/AccountCommands.py
from streamIDs import STREAM_ID_ACCOUNT_CMDS_MIN, STREAM_ID_ACCOUNT_CMDS_MAX
RES_FAILURE = -1
RES_WRONG_ARGS = -2
RES_NON_PLAYER = -3
RES_SHOP_DESYNC = -4
RES_COOLDOWN = -5
RES_HIDDEN_DOSSIER = -6
RES_CENTER_DISCONNECTED = -7
RES_TUTORIAL_DISABLED = -8
RES_STEAM_DISABLED = -9
RES_NOT_AVAILABLE = -10
RES_SUCCESS = 0
RES_STREAM = 1
RES_CACHE = 2

def isCodeValid(code):
    return code >= 0


CMD_RESERVED = 0
CMD_SYNC_DATA = 100
CMD_EQUIP = 101
CMD_EQUIP_OPTDEV = 102
CMD_EQUIP_SHELLS = 103
CMD_EQUIP_EQS = 104
CMD_EQUIP_TMAN = 105
CMD_REPAIR = 106
CMD_VEH_SETTINGS = 107
CMD_SET_AND_FILL_LAYOUTS = 108
CMD_VEH_CAMOUFLAGE = 120
CMD_VEH_HORN = 121
CMD_VEH_EMBLEM = 122
CMD_VEH_INSCRIPTION = 123
CMD_SELECT_POTAPOV_QUESTS = 124
CMD_GET_POTAPOV_QUEST_REWARD = 125
CMD_BUY_POTAPOV_QUEST_TILE = 126
CMD_BUY_POTAPOV_QUEST_SLOT = 127
CMD_TMAN_ADD_SKILL = 151
CMD_TMAN_DROP_SKILLS = 152
CMD_TMAN_RESPEC = 153
CMD_TMAN_PASSPORT = 154
CMD_TRAINING_TMAN = 155
CMD_TMAN_MULTI_RESPEC = 156
CMD_RETURN_CREW = 157
CMD_TMAN_CHANGE_ROLE = 158
CMD_UNLOCK = 201
CMD_EXCHANGE = 202
CMD_FREE_XP_CONV = 203
CMD_PREMIUM = 204
CMD_BUY_SLOT = 205
CMD_BUY_BERTHS = 206
CMD_SYNC_SHOP = 300
CMD_BUY_VEHICLE = 301
CMD_BUY_ITEM = 302
CMD_BUY_TMAN = 303
CMD_SELL_VEHICLE = 304
CMD_SELL_ITEM = 305
CMD_DISMISS_TMAN = 306
CMD_VERIFY_FIN_PSWD = 307
CMD_BUY_AND_EQUIP_ITEM = 308
CMD_BUY_AND_EQUIP_TMAN = 309
CMD_PRB_JOIN = 400
CMD_PRB_LEAVE = 401
CMD_PRB_READY = 402
CMD_PRB_NOT_READY = 403
CMD_PRB_ASSIGN = 404
CMD_PRB_SWAP_TEAM = 405
CMD_PRB_CH_ARENA = 406
CMD_PRB_CH_ROUND = 407
CMD_PRB_OPEN = 408
CMD_PRB_CH_COMMENT = 409
CMD_PRB_CH_ARENAVOIP = 410
CMD_PRB_TEAM_READY = 411
CMD_PRB_TEAM_NOT_READY = 412
CMD_PRB_KICK = 414
CMD_PRB_CH_DIVISION = 415
CMD_PRB_CH_GAMEPLAYSMASK = 416
CMD_PRB_ACCEPT_INVITE = 417
CMD_PRB_DECLINE_INVITE = 418
CMD_REQ_SERVER_STATS = 501
CMD_REQ_QUEUE_INFO = 502
CMD_REQ_PLAYER_INFO = 503
CMD_REQ_ACCOUNT_DOSSIER = 504
CMD_REQ_VEHICLE_DOSSIER = 505
CMD_REQ_PLAYER_CLAN_INFO = 506
CMD_REQ_PLAYER_GLOBAL_RATING = 507
CMD_REQ_PLAYERS_GLOBAL_RATING = 508
CMD_REQ_PREBATTLES = 520
CMD_REQ_PREBATTLES_BY_CREATOR = 521
CMD_REQ_PREBATTLES_BY_DIVISION = 522
CMD_REQ_PREBATTLE_ROSTER = 523
CMD_SYNC_DOSSIERS = 600
CMD_ENQUEUE_RANDOM = 700
CMD_DEQUEUE_RANDOM = 701
CMD_ENQUEUE_TUTORIAL = 702
CMD_DEQUEUE_TUTORIAL = 703
CMD_ENQUEUE_UNIT_ASSEMBLER = 704
CMD_DEQUEUE_UNIT_ASSEMBLER = 705
CMD_ENQUEUE_HISTORICAL = 706
CMD_DEQUEUE_HISTORICAL = 707
CMD_ENQUEUE_EVENT_BATTLES = 708
CMD_DEQUEUE_EVENT_BATTLES = 709
CMD_ACCEPT_TRADE_OFFER = 801
CMD_DECLINE_TRADE_OFFER = 802
CMD_REVOKE_TRADE_OFFER = 803
CMD_CAPTCHA_CHALLENGE = 900
CMD_SET_LANGUAGE = 1000
CMD_MAKE_DENUNCIATION = 1100
CMD_COMPLETE_TUTORIAL = 1150
CMD_STEAM_INIT_TXN = 1200
CMD_STEAM_FINALIZE_TXN = 1201
CMD_EBANK_GET_BALANCE = 1300
CMD_EBANK_BUY_GOLD = 1301
CMD_BAN_UNBAN_USER = 1400
CMD_REQ_BATTLE_RESULTS = 1500
CMD_BATTLE_RESULTS_RECEIVED = 1501
CMD_ADD_INT_USER_SETTINGS = 1600
CMD_DEL_INT_USER_SETTINGS = 1601
CMD_GET_AVATAR_SYNC = 1602
CMD_LOG_CLIENT_UX_EVENTS = 1603
CMD_LOG_CLIENT_XMPP_EVENTS = 1604
CMD_DO_CLUB_CMD = 1700
CMD_NOTIFICATION_REPLY = 1800
CMD_SET_MONEY = 10001
CMD_ADD_XP = 10002
CMD_ADD_TMAN_XP = 10003
CMD_UNLOCK_ALL = 10004
CMD_FORCE_QUEUE = 10008
CMD_INVITATION_ACCEPT = 10010
CMD_INVITATION_DECLINE = 10011
CMD_INVITATION_SEND = 10012
CMD_ACTIVATE_GOODIE = 10013
CMD_NAMES = dict([ (v, k) for k, v in globals().items() if k.startswith('CMD_') ])

class LOCK_REASON:
    NONE = 0
    ON_ARENA = 1
    IN_QUEUE = 2
    PREBATTLE = 4
    UNIT = 8
    UNIT_CLUB = UNIT | 16


LOCK_REASON_NAMES = dict([ (v, k) for k, v in LOCK_REASON.__dict__.items() if not k.startswith('__') ])

class BUY_VEHICLE_FLAG:
    NONE = 0
    CREW = 1
    SHELLS = 16


class VEHICLE_SETTINGS_FLAG:
    NONE = 0
    XP_TO_TMAN = 1
    AUTO_REPAIR = 2
    AUTO_LOAD = 4
    AUTO_EQUIP = 8
    GROUP_0 = 16


REQUEST_ID_PREBATTLES = STREAM_ID_ACCOUNT_CMDS_MIN
REQUEST_ID_PREBATTLE_ROSTER = STREAM_ID_ACCOUNT_CMDS_MIN + 1
REQUEST_ID_NO_RESPONSE = STREAM_ID_ACCOUNT_CMDS_MIN + 2
REQUEST_ID_NON_CLIENT = STREAM_ID_ACCOUNT_CMDS_MIN + 3
REQUEST_ID_UNRESERVED_MIN = STREAM_ID_ACCOUNT_CMDS_MIN + 20
REQUEST_ID_UNRESERVED_MAX = STREAM_ID_ACCOUNT_CMDS_MAX