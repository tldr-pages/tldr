# argos-translate

> 一个用 Python 编写的开源离线翻译库和 CLI 工具。
> 更多信息：<https://argos-translate.readthedocs.io/en/latest/source/cli.html>.

- 安装用于西班牙语到英语翻译的翻译对：

`argospm install translate-es_en`

- 将一些文本从西班牙语（`es`）翻译为英语（`en`）（注意：仅支持两位字母的语言代码）：

`argos-translate --from-lang es --to-lang en {{一段简短的文本}}`

- 将一个文本文件从英语翻译为印地语：

`cat {{路径/到/文件.txt}} | argos-translate --from-lang en --to-lang hi`

- 列出所有已安装的翻译对：

`argospm list`

- 显示可供安装的、从英语出发的翻译对：

`argospm search --from-lang en`

- 更新已安装的语言包翻译对：

`argospm update`

- 从 `ar` 翻译为 `ru`（注意：这需要已安装翻译对 `translate-ar_en` 和 `translate-en_ru`）：

`argos-translate --from-lang ar --to-lang ru {{一张图片胜过千言万语}}`
