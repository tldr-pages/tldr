# clang-tidy

> 基于 LLVM 的 C/C++ 风格检查工具，通过静态分析找到风格违规、错误和安全漏洞。
> 更多信息：<https://clang.llvm.org/extra/clang-tidy/>。

- 对源文件运行默认检查：

`clang-tidy {{path/to/file.cpp}}`

- 除了 `cppcoreguidelines` 检查外，不运行任何其他检查：

`clang-tidy {{path/to/file.cpp}} -checks={{-*,cppcoreguidelines-*}}`

- 列出所有可用的检查：

`clang-tidy -checks={{*}} -list-checks`

- 指定编译选项（在 `--` 之后）以定义宏和包含路径：

`clang-tidy {{path/to/file.cpp}} -- -I{{my_project/include}} -D{{definitions}}`
