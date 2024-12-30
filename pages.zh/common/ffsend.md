# ffsend

> 轻松安全地共享文件。
> 更多信息: <https://gitlab.com/timvisee/ffsend>。

- 上传文件：

`ffsend upload {{path/to/file}}`

- 下载文件：

`ffsend download {{url}}`

- 上传带密码的文件：

`ffsend upload {{path/to/file}} {{-p|--password}} {{password}}`

- 下载受密码保护的文件：

`ffsend download {{url}} {{-p|--password}} {{password}}`

- 上传文件并允许4次下载：

`ffsend upload {{path/to/file}} {{-d|--downloads}} {{4}}`