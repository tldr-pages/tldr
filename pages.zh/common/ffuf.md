# ffuf

> 一个用 Go 语言编写的快速 Web 模糊测试工具。
> `FUZZ` 关键词用作占位符。`ffuf` 会通过将 `FUZZ` 替换为单词列表中的每个单词来尝试访问 URL。
> 更多信息：<https://github.com/ffuf/ffuf#usage>.

- 使用彩色输出和指定的单词列表枚举目录，指定目标 URL：

`ffuf -c -w {{path/to/wordlist.txt}} -u {{http://target/FUZZ}}`

- 通过更改关键词的位置来枚举子域的 Web 服务器：

`ffuf -w {{path/to/subdomains.txt}} -u {{http://FUZZ.target.com}}`

- 使用指定的线程数（默认：40）和代理流量，并将输出保存到文件：

`ffuf -o -w {{path/to/wordlist.txt}} -u {{http://target/FUZZ}} -t {{500}} -x {{http://127.0.0.1:8080}}`

- 使用指定的 HTTP 头部（"名称: 值"）和匹配 HTTP 状态码进行模糊测试：

`ffuf -w {{path/to/wordlist.txt}} -u {{http://target.com}} -H "{{Host: FUZZ}}" -mc {{200}}`

- 使用指定的 HTTP 方法和数据进行模糊测试，同时过滤掉以逗号分隔的状态码：

`ffuf -w {{path/to/postdata.txt}} -X {{POST}} -d "{{username=admin\&password=FUZZ}}" -u {{http://target/login.php}} -fc {{401,403}}`

- 使用不同的模式和多个单词列表对多个位置进行模糊测试：

`ffuf -w {{path/to/keys:KEY}} -w {{path/to/values:VALUE}} -mode {{pitchfork|clusterbomb}} -u {{http://target.com/id?KEY=VALUE}}`

- 通过 HTTP MITM 代理（如 Burp Suite 或 `mitmproxy`）代理请求：

`ffuf -w {{path/to/wordlist}} -x {{http://127.0.0.1:8080}} -u {{http://target.com/FUZZ}}`