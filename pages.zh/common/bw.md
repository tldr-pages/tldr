# bw

> 访问和管理Bitwarden保险箱。
> 更多信息：<https://help.bitwarden.com/article/cli/>。

- 登录到Bitwarden用户账户：

`bw login`

- 从Bitwarden用户账户注销：

`bw logout`

- 搜索并显示Bitwarden保险箱中的项目：

`bw list items --search {{github}}`

- 显示Bitwarden保险箱中的特定项目：

`bw get item {{github}}`

- 在Bitwarden保险箱中创建一个文件夹：

`{{echo -n '{"name":"My Folder1"}' | base64}} | bw create folder`