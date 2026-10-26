# BaiduPCS-Go

> 百度网盘客户端。
> 上传、下载、转存和离线下载。
> 更多信息：<https://github.com/qjfoidnh/BaiduPCS-Go>.

- 使用 BDUSS 和 STOKEN 登录百度网盘账号：

`BaiduPCS-Go login --bduss {{bduss}} --stoken {{stoken}}`

- 下载云端文件或目录到指定的本地目录（省略 `--saveto` 时下载到 `./download/`）：

`BaiduPCS-Go download {{目录/子目录/云端文件或目录1 目录/子目录/云端文件或目录2 ...}} --saveto {{目录/子目录/本地目录}}`

- 上传本地文件或目录到云端目录：

`BaiduPCS-Go upload {{目录/子目录/本地文件或目录1 目录/子目录/本地文件或目录2 ...}} {{目录/子目录/云端目录}}`

- 将分享链接中的文件转存到云端工作目录：

`BaiduPCS-Go transfer {{分享链接}} {{提取码}}`

- 切换云端工作目录：

`BaiduPCS-Go cd {{目录/子目录/云端目录}}`

- 列出云端目录中的文件和目录：

`BaiduPCS-Go ls {{目录/子目录/云端目录}}`

- 进入交互模式：

`BaiduPCS-Go`
