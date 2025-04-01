# bw

> 访问和管理 Bitwarden 保险库。
> 更多信息：<https://help.bitwarden.com/article/cli/>.

- 登录 Bitwarden 用户帐户：

`bw login`

- 登出 Bitwarden 用户帐户：

`bw logout`

- 从 Bitwarden 保险库中搜索并显示项目：

`bw list items --search {{github}}`

- 从 Bitwarden 保险库中显示特定项目：

`bw get item {{github}}`

- 在 Bitwarden 保险库中创建文件夹：

`{{echo -n '{"name":"My Folder1"}' | base64}} | bw create folder`