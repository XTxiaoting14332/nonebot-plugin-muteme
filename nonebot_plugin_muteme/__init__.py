from nonebot.adapters.onebot.v11 import Message, MessageSegment
from nonebot.adapters.onebot.v11 import Bot, Event, GroupMessageEvent, GROUP_ADMIN, GROUP_OWNER
from nonebot.permission import SUPERUSER
import nonebot
import random, re
import datetime
from nonebot.plugin import PluginMetadata,  on_regex
from nonebot.exception import FinishedException


help_text = f"""
muteme
""".strip()

__plugin_meta__ = PluginMetadata(
    name = 'muteme(我禁我自己）',
    description = '高仿@能干辉的muteme',
    usage = help_text
)

muteme = on_regex('^muteme$')
muteme2 = on_regex('^mutemе$')
muteme3 = on_regex('^mutеmе$')
muteme4 = on_regex('^mutеme$')

@muteme.handle()
async def send_msg(bot: Bot, event: GroupMessageEvent):
    user_id = event.get_user_id()
    ban_time = random.randint(1, 900)
    nickname = event.sender.nickname
    now_time = datetime.datetime.now()
    unban_time = now_time + datetime.timedelta(seconds=ban_time)
    unban_time_str = unban_time.strftime("解禁时间:%Y年%m月%d日%H时%M分%S秒")
    try:
        await bot.set_group_ban(group_id=event.group_id, user_id=user_id, duration=ban_time)
    except Exception as e:
        print(e)
        msg = "禁言失败\n[E:Permission denied]"
        await muteme.finish(Message(f'{msg}'), reply_message=False)

    msg = "被禁名称:" + nickname + "\n被禁时间:" + str(ban_time) + "秒\n" + unban_time_str
    await muteme.finish(Message(f'{msg}'), reply_message=False)

whl = on_regex('^我好了$')
@whl.handle()
async def send_msg(bot: Bot, event: GroupMessageEvent):
    user_id = event.get_user_id()
    try:
        await bot.set_group_ban(group_id=event.group_id, user_id=user_id, duration="30")
    except Exception as e:
        print(e)
        msg = "好好好"
        await whl.finish(Message(f'{msg}'), reply_message=False)

    msg = "不许好，憋回去！"
    await whl.finish(Message(f'{msg}'), reply_message=False)



@muteme2.handle()
async def send_msg(bot: Bot, event: GroupMessageEvent):
    user_id = event.get_user_id()
    ban_time = random.randint(1, 900)
    nickname = event.sender.nickname
    now_time = datetime.datetime.now()
    unban_time = now_time + datetime.timedelta(seconds=ban_time)
    unban_time_str = unban_time.strftime("解禁时间:%Y年%m月%d日%H时%M分%S秒")
    try:
        await bot.set_group_ban(group_id=event.group_id, user_id=user_id, duration=ban_time)
    except Exception as e:
        print(e)
        msg = "禁言失败\n[E:Permission denied]"
        await muteme2.finish(Message(f'{msg}'), reply_message=False)

    msg = "被禁名称:" + nickname + "\n被禁时间:" + str(ban_time) + "秒\n" + unban_time_str
    await muteme2.finish(Message(f'{msg}'), reply_message=False)


@muteme3.handle()
async def send_msg(bot: Bot, event: GroupMessageEvent):
    user_id = event.get_user_id()
    ban_time = random.randint(1, 900)
    nickname = event.sender.nickname
    now_time = datetime.datetime.now()
    unban_time = now_time + datetime.timedelta(seconds=ban_time)
    unban_time_str = unban_time.strftime("解禁时间:%Y年%m月%d日%H时%M分%S秒")
    try:
        await bot.set_group_ban(group_id=event.group_id, user_id=user_id, duration=ban_time)
    except Exception as e:
        print(e)
        msg = "禁言失败\n[E:Permission denied]"
        await muteme3.finish(Message(f'{msg}'), reply_message=False)

    msg = "被禁名称:" + nickname + "\n被禁时间:" + str(ban_time) + "秒\n" + unban_time_str
    await muteme3.finish(Message(f'{msg}'), reply_message=False)


@muteme4.handle()
async def send_msg(bot: Bot, event: GroupMessageEvent):
    user_id = event.get_user_id()
    ban_time = random.randint(1, 900)
    nickname = event.sender.nickname
    now_time = datetime.datetime.now()
    unban_time = now_time + datetime.timedelta(seconds=ban_time)
    unban_time_str = unban_time.strftime("解禁时间:%Y年%m月%d日%H时%M分%S秒")
    try:
        await bot.set_group_ban(group_id=event.group_id, user_id=user_id, duration=ban_time)
    except Exception as e:
        print(e)
        msg = "禁言失败\n[E:Permission denied]"
        await muteme4.finish(Message(f'{msg}'), reply_message=False)

    msg = "被禁名称:" + nickname + "\n被禁时间:" + str(ban_time) + "秒\n" + unban_time_str
    await muteme4.finish(Message(f'{msg}'), reply_message=False)

