# ffuf

> 一个用 Go 编写的快速 Web 模糊测试工具。
> `FUZZ` 关键字用作占位符。`ffuf` 将尝试通过用字典中的每个单词替换 `FUZZ` 来访问 URL。
> 更多信息：<https://github.com/ffuf/ffuf#usage>。

- 使用 [c]olor 输出和指定目标 [u]RL 的 [w]ordlist 枚举目录：

`ffuf -c -w {{path/to/wordlist.txt}} -u {{http://target/FUZZ}}`

- 通过改变关键字的位置枚举子域的 web 服务器：

`ffuf -w {{path/to/subdomains.txt}} -u {{http://FUZZ.target.com}}`

- 使用指定的 [t]hreads（默认：40）进行模糊测试，代理流量并将 [o]utput 保存到文件：

`ffuf -o -w {{path/to/wordlist.txt}} -u {{http://target/FUZZ}} -t {{500}} -x {{http://127.0.0.1:8080}}`

- 模糊测试特定 [H]eader（"Name: Value"）并 [m]atch HTTP 状态 [c]odes：

`ffuf -w {{path/to/wordlist.txt}} -u {{http://target.com}} -H "{{Host: FUZZ}}" -mc {{200}}`

- 使用指定的 HTTP 方法和 [d]ata 进行模糊测试，同时 [f]ilter 出逗号分隔的状态 [c]odes：

`ffuf -w {{path/to/postdata.txt}} -X {{POST}} -d "{{username=admin\&password=FUZZ}}" -u {{http://target/login.php}} -fc {{401,403}}`

- 使用不同模式的多个 wordlists 在多个位置进行模糊测试：

`ffuf -w {{path/to/keys:KEY}} -w {{path/to/values:VALUE}} -mode {{pitchfork|clusterbomb}} -u {{http://target.com/id?KEY=VALUE}}`

- 通过 HTTP MITM pro[x]y（如 Burp Suite 或 `mitmproxy`）代理请求：

`ffuf -w {{path/to/wordlist}} -x {{http://127.0.0.1:8080}} -u {{http://target.com/FUZZ}}`