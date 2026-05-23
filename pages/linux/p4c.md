# p4c

> P4 compiler driver.
> Compile P4-14 and P4-16 programs for supported targets and architectures.
> More information: <https://p4lang.github.io/p4c/getting_started.html>.

- Compile a P4-16 program for the BMv2 `simple_switch` using the `v1model` architecture:

`p4c --target bmv2 --arch v1model {{path/to/program.p4}}`

- Compile a P4-14 program for the BMv2 `simple_switch`:

`p4c --target bmv2 --arch v1model --std p4-14 {{path/to/program.p4}}`

- Generate a P4Runtime P4Info file while compiling:

`p4c --target bmv2 --arch v1model --p4runtime-files {{path/to/p4info.txt}} {{path/to/program.p4}}`

- Compile using a specific backend triplet and output path:

`p4c -b {{backend}} {{path/to/program.p4}} -o {{path/to/output}}`

- Add a directory to the include search path:

`p4c --target {{target}} --arch {{architecture}} -I {{path/to/include}} {{path/to/program.p4}}`

- Display supported target and architecture pairs:

`p4c --target-help`
