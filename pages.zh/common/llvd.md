# llvd

> Linkedin学习视频下载器。
> 更多信息：<https://github.com/knowbee/llvd>。

- 使用基于cookie的身份验证下载课程：

`llvd -c {{course-slug}} --cookies`

- 以特定分辨率下载课程：

`llvd -c {{course-slug}} -r 720`

- 下载带有字幕的课程：

`llvd -c {{course-slug}} --caption`

- 在10到30秒之间限速下载课程路径：

`llvd -p {{path-slug}} -t {{10,30}} --cookies`