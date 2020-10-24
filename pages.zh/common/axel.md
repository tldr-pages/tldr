# axel

> 一款下载加速器.
> 支持HTTP, HTTPS, 和 FTP.
> 详见: <https://github.com/axel-download-accelerator/axel>.

- 链接下载:

`axel {{url}}`

- 链接下载，指定文件名:

`axel {{url}} -o {{filename}}`

- 多连接数下载:

`axel -n {{connections_num}} {{url}}`

- 查询镜像:

`axel -S {{mirrors_num}} {{url}}`

- 限制下载速度 (字节bite每秒):

`axel -s {{speed}} {{url}}`
