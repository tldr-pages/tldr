# parallel

> 在多个 CPU 核心上运行命令。
> 更多信息：<https://www.gnu.org/software/parallel>.

- 同时压缩多个文件，使用所有核心：

`parallel gzip ::: {{path/to/file1 path/to/file2 ...}}`

- 从 `stdin` 读取参数，同时运行 4 个任务：

`ls *.txt | parallel -j4 gzip`

- 使用替换字符串将 JPEG 图像转换为 PNG：

`parallel convert {} {.}.png ::: *.jpg`

- 类似于 parallel xargs，尽可能多的将参数塞进一个命令：

`{{args}} | parallel -X {{command}}`

- 将 `stdin` 分割成约 1M 的块，将每个块作为新命令的标准输入：

`cat {{big_file.txt}} | parallel --pipe --block 1M {{command}}`

- 通过 SSH 在多台机器上运行：

`parallel -S {{machine1}},{{machine2}} {{command}} ::: {{arg1}} {{arg2}}`

- 从包含链接的文本文件中同时下载 4 个文件，并显示进度：

`parallel -j4 --bar --eta wget {{[-q|--quote]}} {} :::: {{path/to/links.txt}}`

- 在 `stderr` 中打印 `parallel` 正在运行的任务：

`parallel {{[-t|--verbose]}} {{command}} ::: {{args}}`
