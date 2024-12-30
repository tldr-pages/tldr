# argos-translate

> 一个用Python编写的开源离线翻译库和命令行工具。
> 更多信息请访问：<https://www.argosopentech.com/>.

- 安装西班牙语到英语的翻译对：

`argospm install translate-es_en`

- 将一些文本从西班牙语（`es`）翻译为英语（`en`）（注意：仅支持两个字母的语言代码）：

`argos-translate --from-lang es --to-lang en {{un texto corto}}`

- 将文本文件从英语翻译为印地语：

`cat {{path/to/file.txt}} | argos-translate --from-lang en --to-lang hi`

- 列出所有已安装的翻译对：

`argospm list`

- 显示可安装的英语翻译对：

`argospm search --from-lang en`

- 更新已安装的语言包对：

`argospm update`

- 从阿拉伯语（`ar`）翻译为俄语（`ru`）（注意：这需要安装翻译对 `translate-ar_en` 和 `translate-en_ru`）：

`argos-translate --from-lang ar --to-lang ru {{صورة تساوي أكثر من ألف كلمة}}`