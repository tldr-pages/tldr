# ld

> 将对象文件链接在一起。
> 更多信息：<https://sourceware.org/binutils/docs/ld.html>。

- 将一个没有依赖项的特定目标文件链接到可执行文件中:

`ld {{路径/到/文件.o}} {{[-o|--output]}} {{路径/到/输出_可执行文件}}`

- 将两个目标文件链接在一起:

`ld {{路径/到/文件1.o}} {{路径/到/文件2.o}} {{[-o|--output]}} {{路径/到/输出_可执行文件}}`

- 将x86_64程序动态链接到glibc (文件路径根据系统而变化):

`ld {{[-o|--output]}} {{路径/到/输出_可执行文件}} {{[-I|--dynamic-linker]}} /lib/ld-linux-x86-64.so.2 /lib/crt1.o /lib/crti.o -lc {{路径/到/文件.o}} /lib/crtn.o`
