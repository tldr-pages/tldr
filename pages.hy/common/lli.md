# lli

> Ուղղակիորեն գործարկել ծրագրեր LLVM բիթկոդից:.
> Լրացուցիչ տեղեկություններ. <https://www.llvm.org/docs/CommandGuide/lli.html>:.

- Կատարեք բիթկոդ կամ IR ֆայլ.:

`lli {{path/to/file.ll}}`

- Կատարել հրամանի տողի փաստարկներով.:

`lli {{path/to/file.ll}} {{argument1 argument2 ...}}`

- Միացնել բոլոր օպտիմալացումները.:

`lli -O3 {{path/to/file.ll}}`

- Բեռնել դինամիկ գրադարան նախքան կապելը.:

`lli --dlopen={{path/to/library.dll}} {{path/to/file.ll}}`
