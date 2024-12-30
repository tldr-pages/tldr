# sqlmap

> 检测和利用 SQL 注入漏洞。
> 更多信息：<https://sqlmap.org>。

- 对单个目标 URL 运行 sqlmap：

`python sqlmap.py -u "{{http://www.target.com/vuln.php?id=1}}"`

- 在 POST 请求中发送数据（`--data` 表示 POST 请求）：

`python sqlmap.py -u "{{http://www.target.com/vuln.php}}" --data="{{id=1}}"`

- 更改参数分隔符（& 是默认值）：

`python sqlmap.py -u "{{http://www.target.com/vuln.php}}" --data="{{query=foobar;id=1}}" --param-del="{{;}}"`

- 从 `./txt/user-agents.txt` 中随机选择一个 `User-Agent` 并使用它：

`python sqlmap.py -u "{{http://www.target.com/vuln.php}}" --random-agent`

- 提供用户凭据以进行 HTTP 协议身份验证：

`python sqlmap.py -u "{{http://www.target.com/vuln.php}}" --auth-type {{Basic}} --auth-cred "{{testuser:testpass}}"`