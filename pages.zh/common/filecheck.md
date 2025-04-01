# FileCheck

> 灵活的模式匹配文件验证器。
> 通常用于 LLVM 回归测试，并且是 `lit` 测试的一部分。
> 更多信息：<https://llvm.org/docs/CommandGuide/FileCheck.html>.

- 用模式文件 `check_file` 匹配 `input_file` 内容：

`FileCheck --input-file={{path/to/input_file}} {{path/to/check_file}}`

- 从 `stdin` 读取输入并用模式文件 `check_file` 匹配：

`echo "{{some_text}}" | FileCheck {{path/to/check_file}}`

- 使用指定的自定义检查 `prefix` 进行匹配（注意：默认前缀为 `CHECK`）：

`echo "{{some_text}}" | FileCheck --check-prefix={{prefix}} {{path/to/check_file}}`

- 打印匹配的好的指令模式：

`echo "{{some_text}}" | FileCheck -v {{path/to/check_file}}`

- 将 `llvm_code.ll` 输入到 llvm-as，然后将输出通过 FileCheck 进行匹配：

`llvm-as {{path/to/llvm_code.ll}} | FileCheck {{path/to/check_file}}`