# gfortran

> Նախամշակեք և կազմեք Fortran աղբյուրի ֆայլերը, այնուհետև հավաքեք և կապեք դրանք միասին:.
> Լրացուցիչ տեղեկություններ. <https://gcc.gnu.org/onlinedocs/gfortran/Invoking-GNU-Fortran.html>:.

- Կազմեք բազմաթիվ աղբյուր ֆայլեր գործարկվողի մեջ.:

`gfortran {{path/to/source1.f90 path/to/source2.f90 ...}} -o {{path/to/output_executable}}`

- Ցույց տալ ընդհանուր նախազգուշացումները, վրիպազերծել սիմվոլները ելքում և օպտիմիզացնել՝ առանց վրիպազերծման վրա ազդելու.:

`gfortran {{path/to/source.f90}} -Wall -g -Og -o {{path/to/output_executable}}`

- Ներառեք գրադարաններ այլ ճանապարհից.:

`gfortran {{path/to/source.f90}} -o {{path/to/output_executable}} -I{{path/to/mod_and_include}} -L{{path/to/library}} -l{{library_name}}`

- Կազմել աղբյուրի կոդը Assembler հրահանգների մեջ.:

`gfortran -S {{path/to/source.f90}}`

- Կազմել աղբյուրի կոդը օբյեկտի ֆայլի մեջ՝ առանց կապելու.:

`gfortran -c {{path/to/source.f90}}`
