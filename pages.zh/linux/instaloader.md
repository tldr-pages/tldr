# instaloader

> 从Instagram下载图片、视频、标题和其他元数据。
> 注意：如果您希望下载高质量的媒体，您需要提供Instagram登录信息。
> 更多信息：<https://instaloader.github.io>。

- 下载一个个人资料：

`instaloader {{profile_name}}`

- 下载高亮：

`instaloader --highlights {{profile_name}}`

- 下载带地理标签的帖子（如果可用），并抑制用户交互：

`instaloader --quiet --geotags {{profile_name}}`

- 为HTTP请求指定用户代理：

`instaloader --user-agent {{user_agent}} {{profile_name}}`

- 指定登录信息并下载帖子（对私人资料有用）：

`instaloader --login {{username}} --password {{password}} {{profile_name}}`

- 如果找到第一个下载的文件，则跳过目标（对更新Instagram档案有用）：

`instaloader --fast-update {{profile_name}}`

- 下载故事和IGTV视频（需要登录）：

`instaloader --login {{username}} --password {{password}} --stories --igtv {{profile_name}}`

- 下载所有类型的帖子（需要登录）：

`instaloader --login {{username}} --password {{password}} --stories --igtv --highlights {{profile_name}}`