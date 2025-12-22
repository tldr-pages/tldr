# arduino-builder

> 编译 Arduino 草图。
> 弃用警告：此工具正在逐步淘汰，已由 `arduino` 取代。
> 更多信息：<https://github.com/arduino/arduino-builder>.

- 编译一个草图：

`arduino-builder -compile {{路径/到/草图.ino}}`

- 指定调试级别（默认：5）：

`arduino-builder -debug-level {{1..10}}`

- 指定自定义构建目录：

`arduino-builder -build-path {{路径/到/构建_目录}}`

- 使用构建选项文件，而不是每次手动指定 `-hardware`、`-tools` 等参数：

`arduino-builder -build-options-file {{路径/到/构建.options.json}}`

- 启用详细输出模式：

`arduino-builder -verbose {{true}}`
