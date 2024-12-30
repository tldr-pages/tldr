# clang-tidy

> 一个基于LLVM的C/C++代码检查工具，通过静态分析查找风格违规、错误和安全漏洞。
> 更多信息请访问：<https://clang.llvm.org/extra/clang-tidy/>.

- 在源文件上运行默认检查：

`clang-tidy {{path/to/file.cpp}}`

- 仅在文件上运行`cppcoreguidelines`检查，不运行其他检查：

`clang-tidy {{path/to/file.cpp}} -checks={{-*,cppcoreguidelines-*}}`

- 列出所有可用检查：

`clang-tidy -checks={{*}} -list-checks`

- 将定义和包含指定为编译选项（在`--`之后）：

`clang-tidy {{path/to/file.cpp}} -- -I{{my_project/include}} -D{{definitions}}`