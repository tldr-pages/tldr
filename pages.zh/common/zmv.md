# zmv

> 移动或重命名符合指定扩展模式的文件。
> 请参阅：`zcp` 和 `zln`。
> 更多信息：<https://zsh.sourceforge.net/Doc/Release/User-Contributions.html>.

- 使用类似正则表达式的模式移动文件：

`zmv '{{(*).log}}' '{{$1.txt}}'`

- 预览移动结果，但不进行任何实际更改：

`zmv -n '{{(*).log}}' '{{$1.txt}}'`

- 交互式移动文件，在每次更改之前进行提示：

`zmv -i '{{(*).log}}' '{{$1.txt}}'`

- 在执行时详细打印每个操作：

`zmv -v '{{(*).log}}' '{{$1.txt}}'`
