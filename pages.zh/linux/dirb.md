# dirb

> 扫描基于HTTP的网络服务器以查找目录和文件。
> 更多信息：<https://dirb.sourceforge.net>。

- 使用默认字典扫描网络服务器：

`dirb {{https://example.org}}`

- 使用自定义字典扫描网络服务器：

`dirb {{https://example.org}} {{path/to/wordlist.txt}}`

- 非递归地扫描网络服务器：

`dirb {{https://example.org}} -r`

- 使用指定的用户代理和cookie进行HTTP请求扫描网络服务器：

`dirb {{https://example.org}} -a {{user_agent_string}} -c {{cookie_string}}`