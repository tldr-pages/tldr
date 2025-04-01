# tectonic

> 一个现代的、独立的 TeX/LaTeX 引擎。
> 更多信息：<https://tectonic-typesetting.github.io/book/latest>.

- 编译一个独立的 TeX/LaTeX 文件：

`tectonic -X compile {{path/to/file.tex}}`

- 使用 synctex 数据编译一个独立的 TeX/LaTeX 文件：

`tectonic -X compile --synctex {{path/to/file.tex}}`

- 在当前目录初始化一个 tectonic 项目：

`tectonic -X init`

- 在指定目录初始化一个 tectonic 项目：

`tectonic -X new {{project_name}}`

- 构建当前目录中的项目：

`tectonic -X build`

- 启动一个监控器，在当前目录中的项目发生更改时自动构建：

`tectonic -X watch`
