# shuf

> 生成随机排列。
> 更多信息：<https://www.unix.com/man-page/linux/1/shuf/>.

- 随机化文件中的行顺序并输出结果：

`shuf {{文件名}}`

- 只输出结果的前 5 条：

`shuf --head-count={{5}} {{文件名}}`

- 将结果输出写入另一个文件：

`shuf {{文件名}} --output={{输出_文件名}}`

- 生成范围（1-10）内的随机数：

`shuf --input-range={{1-10}}`
