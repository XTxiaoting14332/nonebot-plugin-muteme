<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-muteme

_✨ 适用于nonebot2 v11的禁言自己插件 高仿 @能干辉 的muteme✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/XTxiaoting14332/nonebot-plugin-muteme.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-muteme">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-muteme.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>



## 📖 介绍

我也不知道我为什么要写出这么无聊的东西...<br>
使用方法非常简单，只需要在群内发送"muteme"即可禁言自己随机时长（默认1-10分钟，如果需要更改请自行修改__init__.py文件）<br>
或者在群里发送“我好了”，会获得一个30秒的禁言


## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令安装

    nb plugin install nonebot-plugin-muteme

</details>

<details>
<summary>pip安装</summary>

    pip install nonebot-plugin-muteme

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_muteme"]
</details>
<details>
<summary>Github下载</summary>
手动克隆本仓库或直接下载压缩包，将里面的nonebot_plugin_muteme文件夹复制到src/plugins中
</details>


</details>

## 🎉 使用
### 指令表(无需指令前缀，直接发送即可)
| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| muteme | 群员 | 否 | 群聊 | Bot需要有管理员权限|
| 我好了 | 群员 | 否 | 群聊 | 无任何说明|
