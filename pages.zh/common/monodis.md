# monodis

> Mono 公共中间语言 (CIL) 反汇编器。
> 更多信息：<https://www.mono-project.com/docs/tools+libraries/tools/monodis/>。

- 将程序集反汇编为文本 CIL：

`monodis {{path/to/assembly.exe}}`

- 将输出保存到文件中：

`monodis --output={{path/to/output.il}} {{path/to/assembly.exe}}`

- 显示有关程序集的信息：

`monodis --assembly {{path/to/assembly.dll}}`

- 列出程序集的引用：

`monodis --assemblyref {{path/to/assembly.exe}}`

- 列出程序集中的所有方法：

`monodis --method {{path/to/assembly.exe}}`

- 列出嵌入程序集中的资源：

`monodis --manifest {{path/to/assembly.dll}}`

- 将所有嵌入的资源提取到当前目录：

`monodis --mresources {{path/to/assembly.dll}}`