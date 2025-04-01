# feroxbuster

> 一个简单、快速的递归内容发现工具，用 Rust 编写。
> 用于对 Web 服务器上的隐藏路径进行暴力破解等。
> 更多信息：<https://epi052.github.io/feroxbuster-docs/docs/>.

- 使用扩展名和 100 个线程以及随机用户代理，发现匹配字典中的特定目录和文件：

`feroxbuster --url "{{https://example.com}}" --wordlist {{path/to/file}} --threads {{100}} --extensions "{{php,txt}}" --random-agent`

- 通过特定代理，不递归地枚举目录：

`feroxbuster --url "{{https://example.com}}" --wordlist {{path/to/file}} --no-recursion --proxy "{{http://127.0.0.1:8080}}"`

- 在网页中查找链接：

`feroxbuster --url "{{https://example.com}}" --extract-links`

- 按特定状态码和字符数过滤：

`feroxbuster --url "{{https://example.com}}" --filter-status {{301}} --filter-size {{4092}}`
