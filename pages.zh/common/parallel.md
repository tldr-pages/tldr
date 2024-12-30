# parallel

> 在多个 CPU 核心上运行命令。
> 更多信息：<https://www.gnu.org/software/parallel>。

- 同时压缩多个文件，使用所有核心：

`parallel gzip ::: {{path/to/file1 path/to/file2 ...}}`

- 从 `stdin` 读取参数，同时运行 4 个任务：

`ls *.txt | parallel -j4 gzip`

- 使用替换字符串将 JPEG 图像转换为 PNG：

`parallel convert {} {.}.png ::: *.jpg`

- 并行 xargs，尽可能将多个参数塞入一个命令：

`{{args}} | parallel -X {{command}}`

- 将 `stdin` 拆分成 ~1M 的块，将每个块输入到新命令的 `stdin` 中：

`cat {{big_file.txt}} | parallel --pipe --block 1M {{command}}`

- 通过 SSH 在多台机器上运行：

`parallel -S {{machine1}},{{machine2}} {{command}} ::: {{arg1}} {{arg2}}`

- 从包含链接的文本文件中同时下载 4 个文件，并显示进度：

`parallel -j4 --bar --eta wget -q {} :::: {{path/to/links.txt}}`

- 打印 `parallel` 正在运行的任务到 `stderr`：

`parallel -t {{command}} ::: {{args}}`