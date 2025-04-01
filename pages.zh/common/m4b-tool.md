# m4b-tool

> 合并、拆分和操作带章节的有声读物文件。
> 更多信息：<https://github.com/sandreas/m4b-tool>.

- 使用输入目录中的音频文件创建有声读物：

`m4b-tool merge {{path/to/input_directory}} --output-file={{path/to/merged.m4b}}`

- 使用输入文件的名称作为章节：

`m4b-tool merge {{path/to/input_directory}} --output-file={{path/to/merged.m4b}} --use-filenames-as-chapters`
