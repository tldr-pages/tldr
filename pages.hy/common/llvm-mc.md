# llvm-mc

> LLVM Machine Code Խաղահրապարակ: Այն ապահովում է LLVM մեքենայի կոդի հետ աշխատելու գործիքների մի շարք:.
> LLVM-ի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://llvm.org/docs/CommandGuide/llvm-mc.html>:.

- Հավաքեք հավաքման կոդի ֆայլը օբյեկտի ֆայլի մեջ մեքենայի կոդով.:

`llvm-mc --filetype=obj -o {{path/to/output.o}} {{path/to/input.s}}`

- Ապամոնտաժել օբյեկտի ֆայլը մեքենայի կոդով հավաքման կոդի ֆայլի մեջ.:

`llvm-mc --disassemble -o {{path/to/output.s}} {{path/to/input.o}}`

- Կազմել LLVM բիթ կոդի ֆայլը հավաքման կոդի մեջ.:

`llvm-mc -o {{path/to/output.s}} {{path/to/input.bc}}`

- Հավաքեք հավաքման կոդը `stdin`-ից և ցուցադրեք կոդավորումը՝ `stdout`-ով:

`echo "{{addl %eax, %ebx}}" | llvm-mc -show-encoding -show-inst`

- Ապամոնտաժեք մեքենայի կոդը `stdin`-ից նշված եռակի համար.:

`echo "{{0xCD 0x21}}" | llvm-mc --disassemble -triple={{target_name}}`
