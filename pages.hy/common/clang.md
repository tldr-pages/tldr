# զնգալ

> Կազմել C, C++ և Objective-C աղբյուրի ֆայլերը: Կարող է օգտագործվել որպես GCC-ի կաթիլային փոխարինում:.
> LLVM-ի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://clang.llvm.org/docs/ClangCommandLineReference.html>:.

- Կազմեք բազմաթիվ աղբյուր ֆայլեր գործարկվողի մեջ.:

`clang {{path/to/source1.c path/to/source2.c ...}} {{[-o|--output]}} {{path/to/output_executable}}`

- Ակտիվացրեք բոլոր սխալների և նախազգուշացումների ելքը.:

`clang {{path/to/source.c}} -Wall {{[-o|--output]}} {{output_executable}}`

- Ցույց տալ ընդհանուր նախազգուշացումները, վրիպազերծել սիմվոլները ելքում և օպտիմիզացնել՝ առանց վրիպազերծման վրա ազդելու.:

`clang {{path/to/source.c}} -Wall {{[-g|--debug]}} -Og {{[-o|--output]}} {{path/to/output_executable}}`

- Ներառեք գրադարաններ այլ ճանապարհից.:

`clang {{path/to/source.c}} {{[-o|--output]}} {{path/to/output_executable}} -I{{path/to/header}} -L{{path/to/library}} -l{{library_name}}`

- Կազմել աղբյուրի կոդը LLVM միջանկյալ ներկայացուցչության մեջ (IR):

`clang {{[-S|--assemble]}} -emit-llvm {{path/to/source.c}} {{[-o|--output]}} {{path/to/output.ll}}`

- Կազմել աղբյուրի կոդը օբյեկտի ֆայլի մեջ՝ առանց կապելու.:

`clang {{[-c|--compile]}} {{path/to/source.c}}`

- Օպտիմալացնել կազմված ծրագիրը կատարման համար.:

`clang {{path/to/source.c}} -O{{1|2|3|fast}} {{[-o|--output]}} {{path/to/output_executable}}`

- Ցուցադրման տարբերակը:

`clang --version`
