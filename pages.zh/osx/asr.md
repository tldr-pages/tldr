# asr

> 将磁盘映像还原（复制）到卷上。
> 命令名称是 Apple Software Restore 的缩写。
> 更多信息：<https://keith.github.io/xcode-man-pages/asr.8.html>.

- 将磁盘映像复制到目标卷：

`sudo asr restore --source {{映像名.dmg}} --target {{卷路径}}`

- 在复制之前擦除目标卷：

`sudo asr restore --source {{映像名.dmg}} --target {{卷路径}} --erase`

- 恢复后跳过验证步骤：

`sudo asr restore --source {{映像名.dmg}} --target {{卷路径}} --noverify`

- 不使用中间磁盘映像直接复制卷中的数据：

`sudo asr restore --source {{卷路径}} --target {{复制卷路径}}`
