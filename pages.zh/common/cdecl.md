# cdecl

> 组合和解析 C 和 C++ 类型声明。
> 更多信息：<https://manned.org/cdecl>.

- 将英文短语组合成 C 声明，并生成可编译的输出（包含 `;` 和 `{}`）：

`cdecl -c {{phrase}}`

- 用英文解释 C 声明：

`cdecl explain {{C_declaration}}`

- 将变量转换为另一种类型：

`cdecl cast {{variable_name}} to {{type}}`

- 以交互模式运行：

`cdecl -i`
