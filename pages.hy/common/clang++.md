# cang++

> Կազմել C++ աղբյուրի ֆայլերը:.
> LLVM-ի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://clang.llvm.org/docs/UsersManual.html#command-line-options>:.

- Կազմել սկզբնական կոդի ֆայլերի մի շարք գործարկվող երկուականի մեջ.:

`clang++ {{path/to/source1.cpp path/to/source2.cpp ...}} {{[-o|--output]}} {{path/to/output_executable}}`

- Ակտիվացրեք բոլոր սխալների և նախազգուշացումների ելքը.:

`clang++ {{path/to/source.cpp}} -Wall {{[-o|--output]}} {{output_executable}}`

- Ցույց տալ ընդհանուր նախազգուշացումները, վրիպազերծել սիմվոլները ելքում և օպտիմիզացնել՝ առանց վրիպազերծման վրա ազդելու.:

`clang++ {{path/to/source.cpp}} -Wall {{[-g|--debug]}} -Og {{[-o|--output]}} {{path/to/output_executable}}`

- Ընտրեք լեզվի ստանդարտ՝ կազմելու համար.:

`clang++ {{path/to/source.cpp}} -std={{c++20}} {{[-o|--output]}} {{path/to/output_executable}}`

- Ներառեք գրադարաններ, որոնք գտնվում են աղբյուրի ֆայլից տարբեր ճանապարհով.:

`clang++ {{path/to/source.cpp}} {{[-o|--output]}} {{path/to/output_executable}} -I{{path/to/header_path}} -L{{path/to/library_path}} -l{{path/to/library_name}}`

- Կազմել աղբյուրի կոդը LLVM միջանկյալ ներկայացուցչության մեջ (IR):

`clang++ {{[-S|--assemble]}} -emit-llvm {{path/to/source.cpp}} {{[-o|--output]}} {{path/to/output.ll}}`

- Օպտիմալացնել կազմված ծրագիրը կատարման համար.:

`clang++ {{path/to/source.cpp}} -O{{1|2|3|fast}} {{[-o|--output]}} {{path/to/output_executable}}`

- Ցուցադրման տարբերակը:

`clang++ --version`
