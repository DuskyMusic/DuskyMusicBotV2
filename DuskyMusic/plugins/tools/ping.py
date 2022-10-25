#
# Copyright (C) 2022-2023 by DuskyMusic@Github, < https://github.com/DuskyMusic >.
#
# This file is part of < https://github.com/DuskyMusic/DuskyMusicBotV2 > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DuskyMusic/DuskyMusicBotV2/blob/master/LICENSE >
#
# All rights reserved.

from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL
from strings import get_command
from DuskyMusic import app
from DuskyMusic.core.call import Dusky
from DuskyMusic.utils import bot_sys_stats
from DuskyMusic.utils.decorators.language import language

### Commands
PING_COMMAND = get_command("PING_COMMAND")


@app.on_message(
    filters.command(PING_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def ping_com(client, message: Message, _):
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"],
    )
    start = datetime.now()
    pytgping = await Dusky.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(
            MUSIC_BOT_NAME, resp, UP, DISK, CPU, RAM, pytgping
        )
    )
