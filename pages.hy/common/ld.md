#լդ

> Կապել օբյեկտի ֆայլերը միասին:.
> Լրացուցիչ տեղեկություններ. <https://sourceware.org/binutils/docs/ld.html#Options>:.

- Կցեք կոնկրետ օբյեկտի ֆայլը առանց որևէ կախվածության գործարկվողի մեջ.:

`ld {{path/to/file.o}} {{[-o|--output]}} {{path/to/output_executable}}`

- Միացրեք բազմաթիվ օբյեկտային ֆայլեր միասին.:

`ld {{path/to/file1.o path/to/file2.o ...}} {{[-o|--output]}} {{path/to/output_executable}}`

- Կապել օբյեկտի ֆայլը հատուկ թիրախային էմուլյացիայի հետ.:

`ld {{path/to/file.o}} -m {{target_emulation}} {{[-o|--output]}} {{path/to/output_executable}}`

- Դինամիկ կերպով կապեք x86_64 ծրագիրը glibc-ին (ֆայլի ուղիները փոխվում են՝ կախված համակարգից).:

`ld {{[-o|--output]}} {{path/to/output_executable}} {{[-I|--dynamic-linker]}} {{/lib/ld-linux-x86-64.so.2}} {{/lib/crt1.o}} {{/lib/crti.o}} -lc {{path/to/file.o}} {{/lib/crtn.o}}`
