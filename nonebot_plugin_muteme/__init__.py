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
    name = 'nonebot-plugin-muteme',
    description = '高仿@能干辉的muteme,我禁我自己',
    usage = help_text ,
    type="application",
    homepage="https://github.com/XTxiaoting14332/nonebot-plugin-muteme",
    extra={
        "unique_name": "muteme",
        "example": """muteme""",
        "author": "NightWind",
        "version": "0.0.3-beta",
    },
)

muteme = on_regex('^muteme$')


@muteme.handle()
async def send_msg(bot: Bot, event: GroupMessageEvent):
#获取用户id和昵称
    user_id = event.get_user_id()
    nickname = event.sender.nickname
#随机秒数
    ban_time = random.randint(1, 600)
#计算解封时间
    now_time = datetime.datetime.now()
    unban_time = now_time + datetime.timedelta(seconds=ban_time)
    unban_time_str = unban_time.strftime("解禁时间:%Y年%m月%d日%H时%M分%S秒")
#判断Bot是否有权限禁言，如果无权限则发送[E:Permission denied]
    try:
        await bot.set_group_ban(group_id=event.group_id, user_id=user_id, duration=ban_time)
    except Exception as e:
        print(e)
        msg = "禁言失败\n[E:Permission denied]"
        await muteme.finish(Message(f'{msg}'), reply_message=False)

    msg = "被禁名称:" + nickname + "\n被禁时间:" + str(ban_time) + "秒\n" + unban_time_str
    await muteme.finish(Message(f'{msg}'), reply_message=False)

