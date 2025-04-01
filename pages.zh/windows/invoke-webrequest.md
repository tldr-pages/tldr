# Invoke-WebRequest

> 向 Web 发送 HTTP/HTTPS 请求。
> 注意：此命令只能通过 PowerShell 使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- 下载 URL 的内容到文件：

`Invoke-WebRequest {{http://example.com}} -OutFile {{path\to\file}}`

- 发送表单编码的数据（类型为 `application/x-www-form-urlencoded` 的 POST 请求）：

`Invoke-WebRequest -Method Post -Body @{ name='bob' } {{http://example.com/form}}`

- 使用自定义 HTTP 方法发送带有额外头部的请求：

`Invoke-WebRequest -Headers {{@{ X-My-Header = '123' }}} -Method {{PUT}} {{http://example.com}}`

- 以 JSON 格式发送数据，并指定适当的内容类型头部：

`Invoke-WebRequest -Body {{'{"name":"bob"}'}} -ContentType 'application/json' {{http://example.com/users/1234}}`

- 传递用户名和密码用于服务器认证：

`Invoke-WebRequest -Headers @{ Authorization = "Basic "+ [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes("myusername:mypassword")) } {{http://example.com}}`