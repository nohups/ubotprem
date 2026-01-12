from motor.motor_asyncio import AsyncIOMotorClient

from fansx.config import MONGO_URL

mongo_client = AsyncIOMotorClient(MONGO_URL)
mongodb = mongo_client.userbotxx

from fansx.core.database.expired import *
from fansx.core.database.userbot import *
from fansx.core.database.two_factor import *
from fansx.core.database.pref import *
from fansx.core.database.variabel import *
from fansx.core.database.antigcast import *