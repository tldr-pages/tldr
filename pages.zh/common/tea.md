# tea

> 与 Gitea 服务器交互。
> 更多信息：<https://gitea.com/gitea/tea>.

- 登录到 Gitea 服务器：

`tea login add --name "{{name}}" --url "{{url}}" --token "{{token}}"`

- 显示所有仓库：

`tea repos ls`

- 显示问题列表：

`tea issues ls`

- 显示特定仓库的问题列表：

`tea issues ls --repo "{{repository}}"`

- 创建新问题：

`tea issues create --title "{{title}}" --body "{{body}}"`

- 显示开放的拉取请求列表：

`tea pulls ls`

- 在浏览器中打开当前仓库：

`tea open`
