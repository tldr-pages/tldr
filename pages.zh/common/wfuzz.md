# wfuzz

> 一个网络应用暴力破解工具。
> 更多信息：<https://wfuzz.readthedocs.io/en/latest/user/basicusage.html>。

- 使用指定的 [w]ordlist 进行目录和文件的暴力破解，同时 [p]roxy 代理流量：

`wfuzz -w {{path/to/file}} -p {{127.0.0.1:8080:HTTP}} {{http://example.com/FUZZ}}`

- 将结果保存到 [f]ile：

`wfuzz -w {{path/to/file}} -f {{filename}} {{http://example.com/FUZZ}}`

- 显示 [c]olorized 输出，同时仅显示输出中声明的响应代码：

`wfuzz -c -w {{path/to/file}} --sc {{200,301,302}} {{http://example.com/FUZZ}}`

- 使用自定义 [H]eader 对子域名进行模糊测试，同时 [h]iding 特定的响应 [c]odes 和字数。将 [t]hreads 增加到 100，并包括目标 ip/domain：

`wfuzz -w {{path/to/file}} -H "{{Host: FUZZ.example.com}}" --hc {{301}} --hw {{222}} -t {{100}} {{example.com}}`

- 使用来自文件的用户名和密码列表对基本认证进行暴力破解，针对每个 FUZ[z] 关键词， [h]iding 无效尝试的响应 [c]odes：

`wfuzz -c --hc {{401}} -s {{delay_between_requests_in_seconds}} -z file,{{path/to/usernames}} -z file,{{path/to/passwords}} --basic 'FUZZ:FUZ2Z' {{https://example.com}}`

- 直接从命令行提供词表，并使用 POST 请求进行模糊测试：

`wfuzz -z list,{{word1-word2-...}} {{https://api.example.com}} -d "{{id=FUZZ&showwallet=true}}"`

- 从文件提供词表，并对其应用 base64 和 md5 编码（`wfuzz -e encoders` 列出所有可用编码器）：

`wfuzz -z file,{{path/to/file}},none-base64-md5 {{https://example.com/FUZZ}}`

- 列出可用的编码器/负载/迭代器/打印机/脚本：

`wfuzz -e {{encoders|payloads|iterators|printers|scripts}}`