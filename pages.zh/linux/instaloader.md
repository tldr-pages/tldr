# instaloader

> 从 Instagram 下载图片、视频、标题和其他元数据。
> 注意：如果需要下载高质量媒体，您需要提供 Instagram 登录信息。
> 更多信息：<https://instaloader.github.io>。

- 下载某个个人资料：

`instaloader {{profile_name}}`

- 下载某些高光内容：

`instaloader --highlights {{profile_name}}`

- 下载带有地理标签的帖子（如果可用），并抑制任何用户交互：

`instaloader --quiet --geotags {{profile_name}}`

- 为 HTTP 请求指定用户代理：

`instaloader --user-agent {{user_agent}} {{profile_name}}`

- 指定登录信息并下载帖子（对于私有个人资料有用）：

`instaloader --login {{username}} --password {{password}} {{profile_name}}`

- 如果已下载第一个文件，则跳过目标（对于更新 Instagram 存档有用）：

`instaloader --fast-update {{profile_name}}`

- 下载故事和 IGTV 视频（需要登录）：

`instaloader --login {{username}} --password {{password}} --stories --igtv {{profile_name}}`

- 下载所有类型的帖子（需要登录）：

`instaloader --login {{username}} --password {{password}} --stories --igtv --highlights {{profile_name}}`