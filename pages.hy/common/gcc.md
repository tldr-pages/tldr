# gcc

> Նախամշակեք և կազմեք C և C++ սկզբնաղբյուր ֆայլերը, այնուհետև հավաքեք և կապեք դրանք:.
> GCC-ի մի մասը (GNU Compiler Collection):.
> Լրացուցիչ տեղեկություններ. <https://gcc.gnu.org/onlinedocs/gcc/>:.

- Կազմեք բազմաթիվ աղբյուր ֆայլեր գործարկվողի մեջ.:

`gcc {{path/to/source1.c path/to/source2.c ...}} {{[-o|--output]}} {{path/to/output_executable}}`

- Ակտիվացրեք բոլոր սխալների և նախազգուշացումների ելքը.:

`gcc {{path/to/source.c}} -Wall {{[-o|--output]}} {{output_executable}}`

- Ցույց տալ ընդհանուր նախազգուշացումները, վրիպազերծել սիմվոլները ելքում և օպտիմիզացնել՝ առանց վրիպազերծման վրա ազդելու.:

`gcc {{path/to/source.c}} -Wall {{[-g|--debug]}} -Og {{[-o|--output]}} {{path/to/output_executable}}`

- Ներառեք գրադարաններ այլ ճանապարհից.:

`gcc {{path/to/source.c}} {{[-o|--output]}} {{path/to/output_executable}} -I{{path/to/header}} -L{{path/to/library}} -l{{library_name}}`

- Կազմել աղբյուրի կոդը Assembler հրահանգների մեջ.:

`gcc {{[-S|--assemble]}} {{path/to/source.c}}`

- Կազմել աղբյուրի կոդը օբյեկտի ֆայլի մեջ՝ առանց կապելու.:

`gcc {{[-c|--compile]}} {{path/to/source.c}}`

- Օպտիմալացնել կազմված ծրագիրը կատարման համար.:

`gcc {{path/to/source.c}} -O{{1|2|3|fast}} {{[-o|--output]}} {{path/to/output_executable}}`

- Ցուցադրման տարբերակը:

`gcc --version`
