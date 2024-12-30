# Invoke-WebRequest

> 执行对Web的HTTP/HTTPS请求。
> 注意：此命令只能通过PowerShell使用。
> 更多信息：<https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>。

- 将URL的内容下载到文件中：

`Invoke-WebRequest {{http://example.com}} -OutFile {{path\to\file}}`

- 发送表单编码的数据（类型为`application/x-www-form-urlencoded`的POST请求）：

`Invoke-WebRequest -Method Post -Body @{ name='bob' } {{http://example.com/form}}`

- 使用自定义HTTP方法发送带有额外头部的请求：

`Invoke-WebRequest -Headers {{@{ X-My-Header = '123' }}} -Method {{PUT}} {{http://example.com}}`

- 以JSON格式发送数据，指定适当的内容类型头：

`Invoke-WebRequest -Body {{'{"name":"bob"}'}} -ContentType 'application/json' {{http://example.com/users/1234}}`

- 传递用户名和密码进行服务器身份验证：

`Invoke-WebRequest -Headers @{ Authorization = "Basic "+ [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes("myusername:mypassword")) } {{http://example.com}}`