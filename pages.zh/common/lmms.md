# lmms

> 免费、开源、跨平台的数字音频工作站。
> 渲染 `.mmp` 或 `.mmpz` 项目文件，将 `.mmpz` 文件导出为 XML，或启动图形用户界面。
> 请参阅：`mixxx`。
> 更多信息：<https://lmms.io>。

- 启动图形用户界面：

`lmms`

- 启动图形用户界面并加载外部配置：

`lmms --config {{path/to/config.xml}}`

- 启动图形用户界面并导入 MIDI 或 Hydrogen 文件：

`lmms --import {{path/to/midi/or/hydrogen/file}}`

- 以指定的窗口大小启动图形用户界面：

`lmms --geometry {{x_size}}x{{y_size}}+{{x_offset}}+{{y_offset}}`

- 导出 `.mmpz` 文件：

`lmms dump {{path/to/mmpz/file.mmpz}}`

- 渲染项目文件：

`lmms render {{path/to/mmpz_or_mmp/file}}`

- 渲染项目文件的各个音轨：

`lmms rendertracks {{path/to/mmpz_or_mmp/file}} {{path/to/dump/directory}}`

- 使用自定义采样率、格式和循环渲染：

`lmms render --samplerate {{88200}} --format {{ogg}} --loop --output {{path/to/output/file.ogg}}`