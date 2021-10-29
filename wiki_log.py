# -*- coding: utf-8 -*-
from time import time
import re, os
import asyncio
import hoshino
import time
from os.path import join, getsize
from nonebot import get_bot
from  datetime import datetime
from nonebot import on_command
from hoshino import Service, priv, config
from hoshino.typing import CQEvent
from hoshino.util import DailyNumberLimiter
from . import _song_data, _chip_data

bot = get_bot()

SONG_DATA_LEN = _song_data.SONG_DATA
TIPS_DATA_LEN = _song_data.Muse_Tips
CHIP_DATA_LEN = _chip_data.CHIP_DATA
CHARA_DATA_LEN = _chip_data.CHARA_DATA

wiki_ver = '1.6.0'

_max = 1
_nlmt = DailyNumberLimiter(_max)

sv = Service(
    name = '_MDWIKI_LOG_',
    use_priv = priv.NORMAL,
    manage_priv = priv.SUPERUSER,
    visible = False, #False隐藏
    enable_on_default = True,
    bundle = 'musedash',
    help_ = 'MD百科更新日志'
    )

def getdirsize(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([getsize(join(root, name)) for name in files])
    return size

MD_WIKI_LOG = '''
2021.10.29 更新日志
=====================
【更新】
同步更新MuseDash官方内容。增添了新的歌曲资料（肥宅快乐包vol.13与计划通补完计划一首新曲）

【新增】
新增账号绑定奖励与2021万圣节奖励两张插画。

版本：Version 1.5.3 (242) → Version 1.6.0 (246)
=====================
'''.strip()

@sv.on_fullmatch(["查看百科更新", "检查百科更新", "百科github"])
async def check_github_wiki(bot, ev):
    now = datetime.now()  #获取当前时间
    hour = now.hour  #获取当前时间小时数
    minute = now.minute  #获取当前时间分钟数
    hour_str = f' {hour}' if hour<10 else str(hour)
    minute_str = f' {minute}' if minute<10 else str(minute)
    if not priv.check_priv(ev, priv.ADMIN):
        sv.logger.warning(f"非管理者：{ev.user_id}尝试于{hour_str}点{minute_str}分检查百科更新")
    account = await bot.get_login_info()
    accid = account.get('user_id')
    check = str(accid)
    data = {
        "type": "share",
        "data": {
            "url": "http://github.com/Soung2279/musewiki",
            "title": "MuseDash百科@Github",
            "content": "HoshinoBot插件：MuseDash百科",
            }
        }
    #if check == '756160433':
    #    await bot.send(ev, f"{MD_WIKI_LOG}")
    #else:
    await bot.send(ev, data)
    await bot.send(ev, f"{MD_WIKI_LOG}")


def countFile(dir):
    tmp = 0
    for item in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, item)):
            tmp += 1
        else:
            tmp += countFile(os.path.join(dir, item))
    return tmp

@sv.on_fullmatch(["检查百科文件", "查看百科文件"])
async def check_main_wiki(bot, ev):
    main_path = hoshino.config.RES_DIR  #使用在 _bot_.py 里填入的资源库文件夹
    gid = ev['group_id']
    now = datetime.now()  #获取当前时间
    hour = now.hour  #获取当前时间小时数
    minute = now.minute  #获取当前时间分钟数
    now_date = time.strftime("%Y-%m-%d", time.localtime()) #获取当前日期
    hour_str = f' {hour}' if hour<10 else str(hour)
    minute_str = f' {minute}' if minute<10 else str(minute)
    image_api = await bot.can_send_image()
    record_api = await bot.can_send_record()
    image_check = image_api.get('yes')
    record_check = record_api.get('yes')
    all_songs = len(SONG_DATA_LEN)
    all_tips = len(TIPS_DATA_LEN)
    all_chips = len(CHIP_DATA_LEN)
    all_charas = len(CHARA_DATA_LEN)
    image_all_num = countFile(str(main_path+"img/musewiki/"))
    image_artwork_num = countFile(str(main_path+"img/musewiki/artwork/"))
    image_songcover_num = countFile(str(main_path+"img/musewiki/songcover/"))
    record_all_num = countFile(str(main_path+"record/musewiki/"))
    record_song_demos_num = countFile(str(main_path+"record/musewiki/song_demos/"))
    record_title_num = countFile(str(main_path+"record/musewiki/title/"))
    imgsize = getdirsize(f"{main_path}img/musewiki/")
    recsize = getdirsize(f"{main_path}record/musewiki/")
    img_size_num = '%.3f' % (imgsize / 1024 / 1024)
    rec_size_num = '%.3f' % (recsize / 1024 / 1024)

    text1 = f"【发送权限检查】：\n是否能发送图片:{image_check}\n是否能发送语音:{record_check}"
    text2 = f"【数据存储检查】：\n已录入的歌曲数量:{all_songs}\n已录入的TIPS数量:{all_tips}\n已录入的角色数量:{all_chips}\n已录入的精灵数量:{all_charas}"
    text3 = f"截止{now_date}\n百科存储的图片总数量:{image_all_num}：共计{img_size_num}Mb\n其中插画有{image_artwork_num}张，歌曲封面有{image_songcover_num}张"
    text4 = f"\n百科存储的语音总数量:{record_all_num}：共计{rec_size_num}Mb\n其中试听歌曲有{record_song_demos_num}条，标题语音有{record_title_num}条"

    dict_len = text1 + '\n' + text2
    resources_len = text3 + '\n' + text4

    if not priv.check_priv(ev, priv.ADMIN):
        sv.logger.warning(f"来自群：{gid}的非管理者：{ev.user_id}尝试于{now_date}{hour_str}点{minute_str}分检查百科文件")
        await bot.send(ev, '一般通过群友不需要看这个啦，让管理员来试试看吧')
        return
    else:
        await bot.send(ev, dict_len)
        await bot.send(ev, resources_len)
    if image_songcover_num < all_songs:
        lacknumimg = int(all_songs) - int(image_songcover_num)
        await bot.send(ev, f"歌曲封面图片[songcover]缺失{lacknumimg}张。请联系bot管理员补充资源")
    if record_song_demos_num < all_songs:
        lacknumrec = int(all_songs) - int(record_song_demos_num)
        await bot.send(ev, f"试听歌曲语音[song_demos]缺失{lacknumrec}条。请联系bot管理员补充资源")

GAME_UPDATE_LOG = '''
※更新时间：2021-10-29
※Version 1.6.0 (246)

Happy Halloween!

- 万圣节特别曲包「肥宅快乐包 Vol.13」现已更新，电子幽灵，在线打碟 ( •ω-)✧

- 新增一张节日氛围感十足的插图， 10 月 29 日~ 11 月 4 日上线即可获取，之后可通过升级解锁！等布若把糖都吃掉，就只剩「捣蛋」这一个选项了w

- 嘘——趁大家不注意，「计划通补完计划」偷偷加入了一首新曲……

- 碎片多给、少给、不给的 bug 修复完毕！

- 优化了一些歌曲索引上的小细节，现在可以拖动索引下方滚动条，丝滑找歌了～
'''.strip()

@sv.on_fullmatch(["游戏更新日志", "md官方更新"])
async def official_update_log(bot, ev):
    uid = ev['user_id']
    if not _nlmt.check(uid):
        await bot.send(ev, f"今天已经使用{_max}次了哦~┭┮﹏┭┮呜哇~频繁使用的话bot会宕机的...")
        return
    else:
        await bot.send(ev, GAME_UPDATE_LOG)
    _nlmt.increase(uid)