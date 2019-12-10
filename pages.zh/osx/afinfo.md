# afinfo

> 显示音频文件元数据 (Metadata) 详细信息
> 用 `afinfo --help` 或者 `afinfo -h` 显示完整用法

- 显示音频文件的详细信息:

`afinfo {{文件}}`

- 显示简化的音频文件信息 (单行):

`afinfo -b {{文件}}`

- 显示音频文件的元数据信息以及其 InfoDictionary 词典:

`afinfo -i {{文件}}`

- 以 xml 格式显示音频文件信息:

`afinfo -x {{文件}}`

- 显示警告信息 (如存在):

`afinfo --warnings {{文件}}`