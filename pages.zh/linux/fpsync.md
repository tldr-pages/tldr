# fpsync

> 通过 SSH 在本地或多个远程工作者上执行多个同步过程。
> 更多信息：<https://www.fpart.org/fpsync/>.

- 递归同步目录到另一个位置：

`fpsync -v {{/path/to/source/}} {{/path/to/destination/}}`

- 递归同步目录，并进行最终清理（启用 rsync 的 `--delete` 选项）：

`fpsync -v -E {{/path/to/source/}} {{/path/to/destination/}}`

- 使用 8 个并发同步任务递归同步目录到目标位置：

`fpsync -v -n 8 -E {{/path/to/source/}} {{/path/to/destination/}}`

- 使用 8 个并发同步任务，在两台远程工作者（machine1 和 machine2）上递归同步目录到目标位置：

`fpsync -v -n 8 -E -w login@machine1 -w login@machine2 -d {{/path/to/shared/directory}} {{/path/to/source/}} {{/path/to/destination/}}`

- 使用 4 个本地工作者，每个工作者每次同步任务最多传输 1000 个文件和 100 MB，递归同步目录到目标位置：

`fpsync -v -n 4 -f 1000 -s $((100 * 1024 * 1024)) {{/path/to/source/}} {{/path/to/destination/}}`

- 递归同步所有目录，但排除特定的 `.snapshot*` 文件（注意：选项和值之间必须用管道字符分隔）：

`fpsync -v -O "-x|.snapshot*" {{/path/to/source/}} {{/path/to/destination/}}`
