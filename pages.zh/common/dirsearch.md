# dirsearch

> Web路径扫描器。
> 更多信息：<https://github.com/maurosoria/dirsearch>。

- 使用常见扩展名扫描Web服务器的常见路径：

`dirsearch --url {{url}} --extensions-list`

- 使用`.php`扩展名扫描Web服务器列表的常见路径：

`dirsearch --url-list {{path/to/url-list.txt}} --extensions {{php}}`

- 使用自定义路径和常见扩展名扫描Web服务器：

`dirsearch --url {{url}} --extensions-list --wordlist {{path/to/url-paths.txt}}`

- 使用Cookie扫描Web服务器：

`dirsearch --url {{url}} --extensions {{php}} --cookie {{cookie}}`

- 使用`HEAD` HTTP方法扫描Web服务器：

`dirsearch --url {{url}} --extensions {{php}} --http-method {{HEAD}}`

- 扫描Web服务器并将结果保存到`.json`文件中：

`dirsearch --url {{url}} --extensions {{php}} --json-report {{path/to/report.json}}`