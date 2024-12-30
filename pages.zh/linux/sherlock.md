# sherlock

> 在社交网络上查找用户名。
> 更多信息：<https://github.com/sherlock-project/sherlock>。

- 在社交网络上搜索特定用户名，并将结果保存到文件中：

`sherlock {{username}} --output {{path/to/file}}`

- 在社交网络上搜索特定用户名，并将结果保存到目录中：

`sherlock {{username1 username2 ...}} --folderoutput {{path/to/directory}}`

- 使用Tor网络在社交网络上搜索特定用户名：

`sherlock --tor {{username}}`

- 在每次请求后通过新的Tor电路进行请求：

`sherlock --unique-tor {{username}}`

- 使用代理在社交网络上搜索特定用户名：

`sherlock {{username}} --proxy {{proxy_url}}`

- 在社交网络上搜索特定用户名，并在默认网页浏览器中打开结果：

`sherlock {{username}} --browse`

- 显示帮助信息：

`sherlock --help`