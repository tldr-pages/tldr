# llvd

> LinkedIn Learning 视频下载器。
> 更多信息：<https://github.com/knowbee/llvd>。

- 使用基于 Cookie 的身份验证下载课程：

`llvd {{[-c|--course]}} {{course-slug}} --cookies`

- 以特定分辨率下载课程：

`llvd {{[-c|--course]}} {{course-slug}} {{[-r|--resolution]}} 720`

- 下载带字幕的课程：

`llvd {{[-c|--course]}} {{course-slug}} {{[-ca|--caption]}}`

- 下载课程路径，并在 10 到 30 秒内进行节流：

`llvd {{[-p|--path]}} {{path-slug}} {{[-t|--throttle]}} {{10,30}} --cookies`
