# FileCheck

> Flexible pattern matching file verifier.
> It is typically used from LLVM regression tests and forms a part of a `lit` test.
> More information: <https://llvm.org/docs/CommandGuide/FileCheck.html>.

- Match `input_file` content with pattern file `check_file`:

`FileCheck --input-file={{path/to/input_file}} {{path/to/check_file}}`

- Match input from the `stdin` with pattern file `check_file`:

`echo "{{some_text}}" | FileCheck {{path/to/check_file}}`

- Match with the specified custom check `prefix` (Note: The default prefix is `CHECK`):

`echo "{{some_text}}" | FileCheck --check-prefix={{prefix}} {{path/to/check_file}}`

- Print good directive pattern matches:

`echo "{{some_text}}" | FileCheck -v {{path/to/check_file}}`

- Input `llvm_code.ll` into llvm-as, then pipe the output into FileCheck to match:

`llvm-as {{path/to/llvm_code.ll}} | FileCheck {{path/to/check_file}}`
