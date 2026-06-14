# g++

> Կազմել C++ աղբյուրի ֆայլերը:.
> GCC-ի մի մասը (GNU Compiler Collection):.
> Լրացուցիչ տեղեկություններ. <https://gcc.gnu.org/onlinedocs/gcc/C_002b_002b-Dialect-Options.html>:.

- Կազմել աղբյուրի կոդի ֆայլը գործարկվող երկուականի մեջ.:

`g++ {{path/to/source1.cpp path/to/source2.cpp ...}} {{[-o|--output]}} {{path/to/output_executable}}`

- Ակտիվացրեք բոլոր սխալների և նախազգուշացումների ելքը.:

`g++ {{path/to/source.cpp}} -Wall {{[-o|--output]}} {{path/to/output_executable}}`

- Ցույց տալ ընդհանուր նախազգուշացումները, վրիպազերծել սիմվոլները ելքում և օպտիմիզացնել՝ առանց վրիպազերծման վրա ազդելու.:

`g++ {{path/to/source.cpp}} -Wall {{[-g|--debug]}} -Og {{[-o|--output]}} {{path/to/output_executable}}`

- Ընտրեք լեզվի ստանդարտ, որը պետք է կազմվի (C++98/C++11/C++14/C++17):

`g++ {{path/to/source.cpp}} -std={{c++98|c++11|c++14|c++17}} {{[-o|--output]}} {{path/to/output_executable}}`

- Ներառեք գրադարաններ, որոնք գտնվում են աղբյուրի ֆայլից տարբեր ճանապարհով.:

`g++ {{path/to/source.cpp}} {{[-o|--output]}} {{path/to/output_executable}} -I{{path/to/header}} -L{{path/to/library}} -l{{library_name}}`

- Կազմել և միացնել բազմաթիվ կոդային ֆայլեր գործարկվող երկուականի մեջ.:

`g++ {{[-c|--compile]}} {{path/to/source1.cpp path/to/source2.cpp ...}} && g++ {{[-o|--output]}} {{path/to/output_executable}} {{path/to/source1.o path/to/source2.o ...}}`

- Օպտիմալացնել կազմված ծրագիրը կատարման համար.:

`g++ {{path/to/source.cpp}} -O{{1|2|3|fast}} {{[-o|--output]}} {{path/to/output_executable}}`

- Ցուցադրման տարբերակը:

`g++ --version`
