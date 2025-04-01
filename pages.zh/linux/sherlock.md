# sherlock

> 在社交媒体网络上查找用户名。
> 更多信息：<https://github.com/sherlock-project/sherlock>.

- 在社交媒体网络上搜索特定用户名并将结果保存到文件：

`sherlock {{username}} --output {{path/to/file}}`

- 在社交媒体网络上搜索特定用户名并将结果保存到目录中：

`sherlock {{username1 username2 ...}} --folderoutput {{path/to/directory}}`

- 使用 Tor 网络在社交媒体网络上搜索特定用户名：

`sherlock --tor {{username}}`

- 每次请求后使用新的 Tor 电路发送请求：

`sherlock --unique-tor {{username}}`

- 使用代理在社交媒体网络上搜索特定用户名：

`sherlock {{username}} --proxy {{proxy_url}}`

- 在社交媒体网络上搜索特定用户名并将结果在默认网页浏览器中打开：

`sherlock {{username}} --browse`

- 显示帮助：

`sherlock --help`
