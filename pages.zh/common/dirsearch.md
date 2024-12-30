# dirsearch

> 网站路径扫描器。
> 更多信息：<https://github.com/maurosoria/dirsearch>。

- 扫描一个web服务器以查找常见路径及其常见扩展名：

`dirsearch --url {{url}} --extensions-list`

- 扫描一组web服务器以查找带有`.php`扩展名的常见路径：

`dirsearch --url-list {{path/to/url-list.txt}} --extensions {{php}}`

- 扫描一个web服务器以查找用户定义的路径及其常见扩展名：

`dirsearch --url {{url}} --extensions-list --wordlist {{path/to/url-paths.txt}}`

- 使用cookie扫描一个web服务器：

`dirsearch --url {{url}} --extensions {{php}} --cookie {{cookie}}`

- 使用`HEAD` HTTP方法扫描一个web服务器：

`dirsearch --url {{url}} --extensions {{php}} --http-method {{HEAD}}`

- 扫描一个web服务器，并将结果保存到`.json`文件中：

`dirsearch --url {{url}} --extensions {{php}} --json-report {{path/to/report.json}}`