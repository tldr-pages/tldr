# wfuzz

> 一个网页应用暴力破解工具。
> 更多信息：<https://wfuzz.readthedocs.io/en/latest/user/basicusage.html>.

- 使用指定的字典文件和代理进行目录和文件的暴力破解：

`wfuzz -w {{path/to/file}} -p {{127.0.0.1:8080:HTTP}} {{http://example.com/FUZZ}}`

- 将结果保存到文件中：

`wfuzz -w {{path/to/file}} -f {{filename}} {{http://example.com/FUZZ}}`

- 仅显示指定的响应码并以彩色输出：

`wfuzz -c -w {{path/to/file}} --sc {{200,301,302}} {{http://example.com/FUZZ}}`

- 使用自定义头部进行子域名暴力破解，同时隐藏特定的响应码和字数。将线程数增加到100，并包含目标IP/域名：

`wfuzz -w {{path/to/file}} -H "{{Host: FUZZ.example.com}}" --hc {{301}} --hw {{222}} -t {{100}} {{example.com}}`

- 从文件中使用用户名和密码列表进行Basic Authentication暴力破解，并隐藏未成功尝试的响应码：

`wfuzz -c --hc {{401}} -s {{delay_between_requests_in_seconds}} -z file,{{path/to/usernames}} -z file,{{path/to/passwords}} --basic 'FUZZ:FUZ2Z' {{https://example.com}}`

- 从命令行直接提供字典，并使用POST请求进行暴力破解：

`wfuzz -z list,{{word1-word2-...}} {{https://api.example.com}} -d "{{id=FUZZ&showwallet=true}}"`

- 从文件中提供字典，并对其应用base64和md5编码（`wfuzz -e encoders`列出所有可用的编码器）：

`wfuzz -z file,{{path/to/file}},none-base64-md5 {{https://example.com/FUZZ}}`

- 列出可用的编码器/负载/迭代器/打印机/脚本：

`wfuzz -e {{encoders|payloads|iterators|printers|scripts}}`