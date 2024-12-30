# mixxx

> 免费和开源的跨平台DJ软件。
> 另见：`lmms`。
> 更多信息：<https://mixxx.org/manual/latest/chapters/appendix.html#command-line-options>。

- 以全屏模式启动Mixxx GUI：

`mixxx --fullScreen`

- 以安全开发者模式启动以调试崩溃：

`mixxx --developer --safeMode`

- 调试故障：

`mixxx --debugAssertBreak --developer --loglevel trace`

- 使用指定的设置文件启动Mixxx：

`mixxx --resourcePath {{mixxx/res/controllers}} --settingsPath {{path/to/settings-file}}`

- 调试自定义控制器映射：

`mixxx --controllerDebug --resourcePath {{path/to/mapping-directory}}`

- 显示帮助：

`mixxx --help`