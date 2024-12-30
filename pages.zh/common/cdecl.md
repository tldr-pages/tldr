# cdecl

> 编写和解码 C 和 C++ 类型声明。
> 更多信息：<https://github.com/paul-j-lucas/cdecl>。

- 将英文短语组成 C 声明，并创建可编译的输出（包括 `;` 和 `{}`）：

`cdecl -c {{phrase}}`

- 用英语解释 C 声明：

`cdecl explain {{C_declaration}}`

- 将变量转换为另一种类型：

`cdecl cast {{variable_name}} to {{type}}`

- 以交互模式运行：

`cdecl -i`