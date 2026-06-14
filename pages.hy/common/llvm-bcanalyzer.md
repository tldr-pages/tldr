# llvm-bcanalyzer

> LLVM Bitcode (`.bc`) անալիզատոր:.
> Լրացուցիչ տեղեկություններ. <https://llvm.org/docs/CommandGuide/llvm-bcanalyzer.html>:.

- Տպել վիճակագրություն Bitcode ֆայլի մասին.:

`llvm-bcanalyzer {{path/to/file.bc}}`

- Տպեք SGML ներկայացում և վիճակագրություն Bitcode ֆայլի մասին.:

`llvm-bcanalyzer -dump {{path/to/file.bc}}`

- Կարդացեք Bitcode ֆայլը `stdin`-ից և վերլուծեք այն.:

`cat {{path/to/file.bc}} | llvm-bcanalyzer`
