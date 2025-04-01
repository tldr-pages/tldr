# cewl

> 从网页内容生成密码破解词典的URL爬虫工具。
> 更多信息：<https://digi.ninja/projects/cewl.php>.

- 从给定的URL生成词典文件，深度为2级链接：

`cewl --depth {{2}} --write {{path/to/wordlist.txt}} {{url}}`

- 从给定的URL生成包含数字的词典，单词长度最少为5个字符：

`cewl --with-numbers --min_word_length {{5}} {{url}}`

- 从给定的URL以调试模式生成词典，包括电子邮件地址：

`cewl --debug --email {{url}}`

- 从给定的URL使用HTTP基本或摘要认证生成词典：

`cewl --auth_type {{basic|digest}} --auth_user {{username}} --auth_pass {{password}} {{url}}`

- 通过代理从给定的URL生成词典：

`cewl --proxy_host {{host}} --proxy_port {{port}} {{url}}`