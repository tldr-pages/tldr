# zmv

> 移动或重命名与指定的扩展 glob 模式匹配的文件。
> 另见 `zcp` 和 `zln`。
> 更多信息：<https://zsh.sourceforge.net/Doc/Release/User-Contributions.html>。

- 使用类似正则表达式的模式移动文件：

`zmv '{{(*).log}}' '{{$1.txt}}'`

- 预览移动的结果，而不进行任何实际更改：

`zmv -n '{{(*).log}}' '{{$1.txt}}'`

- 交互式地移动文件，在每次更改之前提示：

`zmv -i '{{(*).log}}' '{{$1.txt}}'`

- 在执行每个操作时详细打印每个动作：

`zmv -v '{{(*).log}}' '{{$1.txt}}'`