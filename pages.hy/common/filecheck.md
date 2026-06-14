# Ֆայլի ստուգում

> Ճկուն օրինակին համապատասխանող ֆայլի ստուգիչ:.
> Այն սովորաբար օգտագործվում է LLVM ռեգրեսիայի թեստերից և կազմում է `lit` թեստի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://llvm.org/docs/CommandGuide/FileCheck.html>:.

- Համեմատեք `input_file` բովանդակությունը `check_file` օրինաչափության ֆայլի հետ:

`FileCheck --input-file={{path/to/input_file}} {{path/to/check_file}}`

- Համապատասխանեցման մուտքագրումը `stdin`-ից `check_file` օրինաչափության ֆայլի հետ:

`echo "{{some_text}}" | FileCheck {{path/to/check_file}}`

- Համընկնում է նշված մաքսային ստուգման հետ `prefix` (Նշում. լռելյայն նախածանցն է՝ `CHECK`):

`echo "{{some_text}}" | FileCheck --check-prefix={{prefix}} {{path/to/check_file}}`

- Տպել լավ հրահանգների օրինակների համընկնումներ.:

`echo "{{some_text}}" | FileCheck -v {{path/to/check_file}}`

- Մուտքագրեք `llvm_code.ll`-ը llvm-as-ում, այնուհետև թողարկեք ելքը FileCheck՝ համապատասխանելու համար՝:

`llvm-as {{path/to/llvm_code.ll}} | FileCheck {{path/to/check_file}}`
