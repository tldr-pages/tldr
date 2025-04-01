# rtmpdump

> 下载通过 RTMP 协议传输的媒体内容。
> 更多信息：<https://rtmpdump.mplayerhq.hu/>.

- 下载一个文件：

`rtmpdump --rtmp {{rtmp://example.com/path/to/video}} -o {{file.ext}}`

- 从 Flash 播放器下载一个文件：

`rtmpdump --rtmp {{rtmp://example.com/path/to/video}} --swfVfy {{http://example.com/player}} --flashVer "{{LNX 10,0,32,18}}" -o {{file.ext}}`

- 如果连接参数未正确检测，指定连接参数：

`rtmpdump --rtmp {{rtmp://example.com/path/to/video}} --app {{app_name}} --playpath {{path/to/video}} -o {{file.ext}}`

- 从需要引用页的服务器下载一个文件：

`rtmpdump --rtmp {{rtmp://example.com/path/to/video}} --pageUrl {{http://example.com/webpage}} -o {{file.ext}}`
