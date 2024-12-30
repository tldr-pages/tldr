# feroxbuster

> 简单、快速、递归的内容发现工具，用Rust编写。
> 用于对网络服务器上的隐藏路径进行暴力破解等操作。
> 更多信息：<https://epi052.github.io/feroxbuster-docs/docs/>.

- 通过特定的词汇表发现匹配的目录和文件，使用扩展名、100个线程和随机用户代理：

`feroxbuster --url "{{https://example.com}}" --wordlist {{path/to/file}} --threads {{100}} --extensions "{{php,txt}}" --random-agent`

- 通过特定代理枚举目录，不进行递归：

`feroxbuster --url "{{https://example.com}}" --wordlist {{path/to/file}} --no-recursion --proxy "{{http://127.0.0.1:8080}}"`

- 查找网页中的链接：

`feroxbuster --url "{{https://example.com}}" --extract-links`

- 按特定状态码和字符数过滤：

`feroxbuster --url "{{https://example.com}}" --filter-status {{301}} --filter-size {{4092}}`