# htpasswd

> 创建和管理 htpasswd 文件，以使用基本身份验证保护 Web 服务器目录。
> 更多信息：<https://httpd.apache.org/docs/current/programs/htpasswd.html>。

- 创建/覆盖 htpasswd 文件：

`htpasswd -c {{path/to/file}} {{username}}`

- 向 htpasswd 文件添加用户或更新现有用户：

`htpasswd {{path/to/file}} {{username}}`

- 以批处理模式向 htpasswd 文件添加用户，无需交互式密码提示（用于脚本使用）：

`htpasswd -b {{path/to/file}} {{username}} {{password}}`

- 从 htpasswd 文件中删除用户：

`htpasswd -D {{path/to/file}} {{username}}`

- 验证用户密码：

`htpasswd -v {{path/to/file}} {{username}}`

- 显示包含用户名（明文）和密码（md5）的字符串：

`htpasswd -nbm {{username}} {{password}}`