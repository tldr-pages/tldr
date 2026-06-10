# irilog

> Նախամշակում և կազմում է Verilog HDL (IEEE-1364) ծածկագիրը գործարկվող ծրագրերի մեջ՝ մոդելավորման համար:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/iverilog>:.

- Կազմել աղբյուրի ֆայլը գործարկվողի մեջ.:

`iverilog {{path/to/source.v}} -o {{path/to/executable}}`

- Կազմեք աղբյուրի ֆայլը գործարկվողի մեջ՝ ցուցադրելով բոլոր նախազգուշացումները.:

`iverilog {{path/to/source.v}} -Wall -o {{path/to/executable}}`

- Կազմեք և գործարկեք բացահայտորեն օգտագործելով VVP գործարկման ժամանակը.:

`iverilog -o {{path/to/executable}} -tvvp {{path/to/source.v}}`

- Կազմել՝ օգտագործելով Verilog գրադարանի ֆայլերը այլ ճանապարհից.:

`iverilog {{path/to/source.v}} -o {{path/to/executable}} -I{{path/to/library_directory}}`

- Նախամշակեք Verilog կոդը առանց կազմելու.:

`iverilog -E {{path/to/source.v}}`
