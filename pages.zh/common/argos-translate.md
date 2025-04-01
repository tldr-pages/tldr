# argos-translate

> 一个用 Python 编写的开源离线翻译库和命令行工具。
> 更多信息：<https://www.argosopentech.com/>。

- 安装从西班牙语到英语的翻译包：

`argospm install translate-es_en`

- 翻译一些西班牙语（`es`）到英语（`en`）的文本（注意：仅支持两位字母的语言代码）：

`argos-translate --from-lang es --to-lang en {{un texto corto}}`

- 将文本文件从英语翻译成印地语：

`cat {{path/to/file.txt}} | argos-translate --from-lang en --to-lang hi`

- 列出所有已安装的翻译包：

`argospm list`

- 显示可安装的从英语开始的翻译包：

`argospm search --from-lang en`

- 更新已安装的语言包：

`argospm update`

- 从 `ar` 翻译到 `ru`（注意：这需要安装翻译包 `translate-ar_en` 和 `translate-en_ru`）：

`argos-translate --from-lang ar --to-lang ru {{صورة تساوي أكثر من ألف كلمة}}`