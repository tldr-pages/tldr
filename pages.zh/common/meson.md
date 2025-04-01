# meson

> 一个类似于 SCons 的构建系统，使用 Python 作为前端语言，Ninja 作为后端构建工具。
> 更多信息：<https://mesonbuild.com>。

- 使用给定的名称和版本生成一个 C 项目：

`meson init --language={{c}} --name={{myproject}} --version={{0.1}}`

- 使用默认值配置 `builddir`：

`meson setup {{build_dir}}`

- 构建项目：

`meson compile -C {{path/to/build_dir}}`

- 运行项目中的所有测试：

`meson test`

- 显示帮助信息：

`meson --help`

- 显示版本信息：

`meson --version`
