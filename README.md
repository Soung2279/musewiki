<p align="center">
  <a href="https://sm.ms/image/gptjxEmihya6nr4">
    <img src="https://i.loli.net/2021/08/14/gptjxEmihya6nr4.png" alt="musewiki">
  </a>
</p>

<div align="center">

MuseDashWiki
===========================
<div align="left">


→→ **[查看更新日志](#更新日志)**

![Visitors](https://jwenjian-visitor-badge-5.glitch.me/badge?page_id=Soung2279.musewiki.readme)

### 2022/5/15  v future  因本人学业繁忙，暂时宣布跑路，更新与维护无限期延迟。
  
### 功能介绍

适用于``Hoshinobot V2+``的 **MuseDash Wiki插件**

~~不知道 MuseDash 是啥？ [喵斯快跑_百度百科](https://baike.baidu.com/item/%E5%96%B5%E6%96%AF%E5%BF%AB%E8%B7%91/57515152)；[MuseDash官网](http://www.peroperogames.com/)；[MuseDash萌娘百科](https://zh.moegirl.org.cn/Muse_Dash)~~

本项目具备的功能有如下：
- **查询歌曲信息**，包括歌曲BPM，作者，时长等 (部分数据来源[MuseDash官方英文Wiki](https://musedash.fandom.com/wiki/Muse_Dash_Wiki)) ，并支持模糊查询 (输入查询的歌曲名时 若名字不对将自动猜测 并提供正确的歌曲名，*改编自 Hoshinobot 原版的 chara*)
- **每日随机推送歌曲/插画**
- **角色语音试听**，包括触摸语音，受击语音等
- **peropero标题语音**  ~~peropero\~games\~~~
- **游戏demo试听**  ~~就是选歌界面播放的歌曲片段~~
- **游戏音效试听**  ~~各种游戏使用的音效，来源拆包数据~~
- **游戏资料查询**，包括分数公式，隐藏曲目，偏移值，表情包等
- **每日运势**  ~~简易实现的md版每日运势抽签~~
- **查询角色与精灵**  ~~muses and elfins~~
- **插图/动画/场景查询**  
- **单曲成就 or 游戏成就查询**
- **官方公告查询**
- ……

在以下环境下，插件已经过测试：
- [x] ``Windows 10``
- [x] ``Windows 11``
- [x] ``python 3.8.5 32&64bit``
- [x] ``python 3.8.9 32&64bit``
- [x] ``Hoshinobot V2.0``
- [ ] 理论上支持 ``Linux``，``python 3.9``，``nonebot 1.6.0+``

[![OS](https://img.shields.io/badge/Windows10-0078d6?style=flat-square&logo=windows&logoColor=fff)](https://www.microsoft.com/zh-cn/windows)  [![Python](https://img.shields.io/badge/Python-yellow?style=flat-square&logo=python)](https://www.python.org/)

> 由于本人不熟悉Linux环境，且插件均在Windows环境下编写完成，在Linux上使用可能有bug，请见谅

**不适用于 ``nonebot2`` ！** ~~（其实是不知道咋从nb1迁移到nb2）~~

### 插件安装

<details>
  <summary>通过github克隆</summary>

在**hoshino/modules**文件夹中，打开cmd或者powershell，输入以下代码按回车执行：

```powershell
git clone https://github.com/Soung2279/musewiki.git
```

之后关闭cmd或powershell，打开**hoshino/config**的`__bot__.py`文件，在**MODULES_ON** = {}里添加 ``musewiki``
```python
# 启用的模块
MODULES_ON = {
    'xxx',
    'xxx',
    'musewiki',  #注意英文逗号！
    'xxx',
}
```

之后将本文件夹中的 ``R.py`` 移动至 ``hoshino`` 路径下（覆盖原来的 R.py）

如果未在本文件夹下找到 ``R.py`` ，可前往→→  [HoshinoBot功能性增强-语音调用支持](https://github.com/Soung2279/advance_R)

</details>

<details>
  <summary>直接安装</summary>

直接下载本插件[musewiki](https://github.com/Soung2279/musewiki/archive/refs/heads/master.zip)，解压至**hoshino/modules**

之后打开**hoshino/config**的`__bot__.py`文件，在**MODULES_ON** = {}里添加advance_check
```python
# 启用的模块
MODULES_ON = {
    'xxx',
    'xxx',
    'advance_check',  #注意英文逗号！
    'xxx',
    'xxx',
}
```

之后将本文件夹中的 ``R.py`` 移动至 ``hoshino`` 路径下（覆盖原来的 R.py）

如果未在本文件夹下找到 ``R.py`` ，可前往→→  [HoshinoBot功能性增强-语音调用支持](https://github.com/Soung2279/advance_R)

</details>


插件安装完成后，**仅**可使用**歌曲/角色/精灵查询**的基础功能。由于本插件使用了大量图片与语音资源 ，需要进行资源包的补充。

<details>
  <summary>Releases</summary>

  →→ [Github项目Releases](https://github.com/Soung2279/musewiki/releases)

</details>

<details>
  <summary>百度网盘</summary>
 
 - [语音资源包 - 1.6g](https://pan.baidu.com/s/1uu8NpD6GT2RxWaVS_K4o8A)
 > 包含demo歌曲，角色语音，菜单bgm等
 > 提取码：2279
 > 更新时间：2021/9/4

 - [图片资源包 - 952mb](https://pan.baidu.com/s/1RJgK26UIDoKxRYGsPXq_cQ)
 > 包含歌曲封面图片，角色/精灵图片，UI等
 > 提取码：2279
 > 更新时间：2021/9/4
  
</details>

<details>
  <summary>QQ群文件</summary>
 
 - [点击链接加入群聊【SoungBot交流群（free edition】](https://jq.qq.com/?_wv=1027&k=DXw3Feqg)
 > 请在群文件中自助下载
  
</details>

### 指令

##### 歌曲查询
- **详细查询+歌名**  详细查询单曲的各种信息，并发送对应的demo
- **随机歌曲信息**  随机查看一条歌曲信息
- **帮助百科歌曲推送**  配置每日的md歌曲推送
##### 角色语音查询
- **摸摸+角色皮肤名**  摸摸角色的头(。・・)ノ
- **打打+角色名**  打一下角色（好过分ヽ(*。>Д<)o゜）
- **随机角色语音**  随便听一句
##### demo查询
- **peropero**  随机播放一条起始(peropero\~games\~)语音
- **随机demo**  随便听一首demo
##### 游戏音效查询
- **随机游戏音效**  随便听听
- **听听好东西**  听一点MD玩家都喜欢听的
##### 资料查询
- **md官方更新** 查看MuseDash官方更新公告  new！
- **查询隐藏曲目**  查询隐藏曲目的解锁方式
- **偏移值参考**  查询游戏偏移值设定参考
- **游戏冷知识**  游戏相关的一些小知识
- **md表情包**  来一张musedash相关的表情包
- **md运势**  查看今天的md运势吧！
##### 角色&精灵查询
- **查询角色**  查询游戏内角色
- **查询精灵**  查询游戏内精灵
##### 插图查询
- **查询插图**  进入插图查询菜单
- **单/全图查询**  不同模式的插图查询
- **动画查询**  查询游戏Live2D插画
- **随机插画/封面**  随机查看一张图片
##### 场景查询
- **查询游戏场景**  进入游戏场景查询菜单
- **纯/合成场景**  查看不同的场景图片
- **随机纯场景/合成场景**  随机查看一张图片
##### 成就查询
- **查询成就**  进入查询菜单
- **单曲成就查询**  查询单曲关卡成就
- **游戏成就查询**  查询游戏成就
##### 运行
- **检查百科文件**  管理员 or 维护用，检查资源文件存储情况  new！


### 说明

**语音资源包** 与 **图片资源包** 请放在HoshinoBot的 ``record`` 和 ``img`` 目录下

例如：你在**hoshino/config**的 `__bot__.py` 文件中填写的 **资源库文件夹**
```python
RES_DIR = "C:/Resources/"  #注意最后有斜杠
```
那么你存放 ``语音资源包`` 的路径应该为

``C:/Resources/record/``

**图片同理**

<details>
  <summary>文件说明（可略）</summary>

``_chip_data.py`` 是游戏角色&精灵 的录入数据 **如果需要自行增添条目，请在此处修改**

``_record_data.py`` 是语音字幕与角色语音的对应  **如果需要自行增添条目，请在此处修改**

``_song_data.py``  是歌曲/小贴士的录入数据  **如果需要自行增添条目，请在此处修改**

``chara.py``  与歌名猜测功能相关，是对Hoshinobot原版chara的改编

``musewiki_achievement.py``  查询成就的主文件

``musewiki_artwork.py``  查询插画的主文件

``musewiki_character.py``  查询角色的主文件

``musewiki_luck.py``  md运势的主文件

``musewiki_query.py``  资料库主文件

``musewiki_record.py``  游戏语音的主文件

``musewiki_song.py`` 是查询歌曲的主文件

``wiki_log.py``  检查百科文件的主文件

``R.py`` R模块增强版，让Hoshinobot支持模块语音调用

</details>


### 其它

资源文件出自个人游戏拆包。文件名有所修改 ~~（后续会进行项目重构，直接使用原版拆包数据）~~
本人非专业程序员，业余写着玩玩，代码很菜，大佬们看看就好QwQ。
made by [Soung2279@Github](https://github.com/Soung2279/)

### 鸣谢

数据来源：
[TapTap - MuseDash](https://www.taptap.com/app/60809)
[MuseDash官方英文Wiki](https://musedash.fandom.com/wiki/Muse_Dash_Wiki)
[MuseDash.moe](https://musedash.moe/)
[PeroPeroGames！](http://www.peroperogames.com/)
[远哥制造](https://lab.yangezhizao.cn/musedash)

骨干：
[HoshinoBot](https://github.com/Ice-Cirno/HoshinoBot)

****

### 更新日志


#### 2021/10/29  Version 1.6.0 (246)

【更新】
同步更新MuseDash官方内容。增添了新的歌曲资料（肥宅快乐包vol.13与计划通补完计划一首新曲）

【新增】
新增账号绑定奖励与2021万圣节奖励两张插画。

#### 2021/9/4  Version 1.5.3 (242)

【新】
版本号同步为游戏官方版本号

【更新】
同步更新MuseDash官方内容。增添了新的角色，插图与歌曲资料

【修复】
修复部分曲包和歌曲缺失问题

#### 2021/9/4  v1.0.6

【修复】
修复了歌曲查询与推送，动画查询功能遗留的绝对路径使用问题  ~~(现在应该完全适配Linux了)~~
修复了动画查询输入超出范围的编号时，bot无响应的问题
修复了部分功能使用冷却/上限无效的问题

【更新】
同步更新MuseDash官方内容。增添了新的精灵，插图与歌曲资料
同步更新曲包UI
同步更新歌曲：Brain Power的封面
更新检查百科文件功能，现在将返回更详细的信息

【新增】
官方更新公告查看功能上线。发送【md官方更新】来查看

※【预更新】 ~~（遥遥无期）~~
重构资料库，增加更多可查信息
重构歌曲曲包分类系统，同步游戏内更新，按“热门”，“复古”，“动感”等重新贴标签
重构资料库储存方式，使用拆包JSON数据，便于日后更新

新版本的图片/语音 资源包请访问Github项目

#### 2021/8/26  v1.0.5

增加对 R模块 语音调用的支持。[[#HoshinoBot功能性增强-语音调用支持](https://github.com/Soung2279/advance_R)]
去除发送语音绝对路径的使用。

#### 2021/8/15  v1.0.0

正式上传至Github仓库

#### 2021/8/14  v0.0.9

补充demo资源

#### 2021/8/11  v0.0.6

修复部分 资料查询 文本缺失
补充部分图片资源
修复动画查询

#### 2021/8/7  v0.0.5

新增：【md运势】  简易实现md每日运势
补充了游戏解包资源，固定文件目录结构

