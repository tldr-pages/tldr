# base64

> 将文件或标准输入编码到 Base64 或从 Base64 解码为标准输出。
> 更多信息：<https://www.gnu.org/software/coreutils/base64>.

- 编码一个文件：

`base64 {{文件名}}`

- 解码一个文件：

`base64 --decode {{文件名}}`

- 从标准输入编码：

`{{某指令}} | base64`

- 将标准输入解码：

`{{某指令}} | base64 --decode`
