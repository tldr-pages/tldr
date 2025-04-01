# quickemu

> 快速构建和管理高度优化的桌面虚拟机。
> 参见：`quickget`，用于准备虚拟机配置。
> 更多信息：<https://github.com/quickemu-project/quickemu>。

- 从配置文件创建并运行虚拟机：

`quickemu --vm {{path/to/file.conf}}`

- 不在磁盘/快照中提交任何更改，而是将任何更改写入临时文件：

`quickemu --status-quo --vm {{path/to/file.conf}}`

- 以全屏模式启动虚拟机（使用`<Ctrl Alt f>`退出）并选择显示后端（默认为`sdl`）：

`quickemu --fullscreen --display {{sdl|gtk|spice|spice-app|none}} --vm {{path/to/file.conf}}`

- 选择要模拟的虚拟音频设备并创建桌面快捷方式：

`quickemu --sound-card {{intel-hda|ac97|es1370|sb16|none}} --shortcut --vm {{path/to/file.conf}}`

- 创建快照：

`quickemu --snapshot create {{tag}} --vm {{path/to/file.conf}}`

- 恢复快照：

`quickemu --snapshot apply {{tag}} --vm {{path/to/file.conf}}`

- 删除快照：

`quickemu --snapshot delete {{tag}} --vm {{path/to/file.conf}}`