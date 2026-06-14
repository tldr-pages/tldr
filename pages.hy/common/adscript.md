# adscript

> Կազմող Adscript ֆայլերի համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/Amplus2/Adscript>:.

- Կազմել ֆայլը օբյեկտի ֆայլի մեջ.:

`adscript --output {{path/to/file.o}} {{path/to/input_file.adscript}}`

- Կազմել և կապել ֆայլը ինքնուրույն գործարկվողի հետ.:

`adscript --executable --output {{path/to/file}} {{path/to/input_file.adscript}}`

- Կազմել ֆայլը LLVM IR-ում` հայրենի մեքենայի կոդի փոխարեն.:

`adscript --llvm-ir --output {{path/to/file.ll}} {{path/to/input_file.adscript}}`

- Փոխադրել ֆայլը օբյեկտի ֆայլին օտար CPU ճարտարապետության կամ օպերացիոն համակարգի համար.:

`adscript --target-triple {{i386-linux-elf}} --output {{path/to/file.o}} {{path/to/input_file.adscript}}`
