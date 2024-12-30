# cewl

> 从网络内容生成破解词表的URL爬虫工具。
> 更多信息：<https://digi.ninja/projects/cewl.php>。

- 从给定的URL创建一个最多链接深度为2的词表文件：

`cewl --depth {{2}} --write {{path/to/wordlist.txt}} {{url}}`

- 从给定的URL输出一个包含最少5个字符的字母数字词表：

`cewl --with-numbers --min_word_length {{5}} {{url}}`

- 在调试模式下从给定的URL输出一个包含电子邮件地址的词表：

`cewl --debug --email {{url}}`

- 从给定的URL使用HTTP基本或摘要认证输出词表：

`cewl --auth_type {{basic|digest}} --auth_user {{username}} --auth_pass {{password}} {{url}}`

- 通过代理从给定的URL输出词表：

`cewl --proxy_host {{host}} --proxy_port {{port}} {{url}}`