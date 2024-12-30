# meson

> 类似SCons的构建系统，使用Python作为前端语言，Ninja作为构建后端。
> 更多信息请访问：<https://mesonbuild.com>。

- 生成一个具有给定名称和版本的C项目：

`meson init --language={{c}} --name={{myproject}} --version={{0.1}}`

- 使用默认值配置 `builddir`：

`meson setup {{build_dir}}`

- 构建项目：

`meson compile -C {{path/to/build_dir}}`

- 运行项目中的所有测试：

`meson test`

- 显示帮助信息：

`meson --help`

- 显示版本：

`meson --version`