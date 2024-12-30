# 折叠

> 为固定宽度输出设备折叠长行。
> 更多信息：<https://www.gnu.org/software/coreutils/fold>。

- 在固定宽度下折叠行：

`fold --width {{宽度}} {{路径/到/文件}}`

- 以字节为单位计算宽度（默认是按列计算）：

`fold --bytes --width {{字节数}} {{路径/到/文件}}`

- 在宽度限制内，在最右侧的空白处断行：

`fold --spaces --width {{宽度}} {{路径/到/文件}}`