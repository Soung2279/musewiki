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

wiki_ver = '1.0.5'

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
2021.9.4 bot更新日志
=====================
【修复】
修复了歌曲查询与推送，动画查询功能遗留的绝对路径使用问题
修复了动画查询输入超出范围的编号时，bot无响应的问题
修复了部分功能使用冷却/上限无效的问题

【更新】
同步更新MuseDash官方内容。增添了新的精灵，插图与歌曲资料
同步更新曲包UI
同步更新歌曲：Brain Power的封面
更新检查百科文件功能，现在将返回更详细的信息

【新增】
官方更新公告查看功能上线。发送【md官方更新】来查看

※【预更新】
重构资料库，增加更多可查信息
重构歌曲曲包分类系统，同步游戏内更新，按“热门”，“复古”，“动感”等重新贴标签
重构资料库储存方式，使用拆包JSON数据，便于日后更新

新版本的图片/语音 资源包请访问Github项目

版本：V1.0.5 → 1.0.6
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
※更新时间：2021-9-3
※Version 1.5.1 (237)

Ready Get Set Go！

1. 节奏医生 X Muse Dash X 冰与火之舞三重联动！联动曲包「7th Beat Games」急速更新！！拥有该曲包即可额外解锁精灵「佩奇医生」+ 一张联动插图！(　ﾟ 3ﾟ) 是新来的护士三人组吗，好大...的医药箱

2. 全新精灵上线！第一只联动精灵出现力，每连击 7 次就会有特殊 buff 加成，带着它斩获 S 评分吧~

3. 特殊谱面演出效果 Get√，1234567，病人竟是我自己⊂彡☆))∀`)

4. 全新标签系统上线力！

5. 「Brain Power」曲绘更换，脑力值提升

热知识：「超·东方不眠夜」默认显示里谱，首次游玩后即可返回到表谱~
长按「超·东方不眠夜」歌曲封面按钮，就能再次进入里世界 (σﾟ∀ﾟ)σ

速速更新，大家一起做小鸡孵化大师（指获得新的精灵
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