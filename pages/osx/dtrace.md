# dtrace

> Generic front-end to DTrace facility.
> This command is a simple interface to invoke the D language compiler, retrieve buffered trace data from the DTrace kernel facility, and a set of basic routines to format and print traced data.
> This requires root privileges.
> More information: <https://www.unix.com/man-page/osx/1/dtrace/>.

- Set dtrace's target data model which is the target architecture:

`dtrace -arch {{arch_name}}`

- Claim anonymous tracing state and display the traced data:

`dtrace -a`

- Set principal trace buffer size. Trace buffer size can include any size suffix like k, m, g or t:

`dtrace -b {{buffer_size}}`

- Compile the specified D Program:

`dtrace -s {{D_script}}`

- Run tghe specified command and exit upon its completion:

`dtrace -c {{path/to/command}}`

- Specify function name to trace or list (-l option).  The corresponding argument can include any of the probe description  forms like provider:module:function, module:function or function:

`dtrace -f {{function}}`

- Grad the process corresponding to specified pid , cache its symbol table and exit upon completion:

`dtrace -p {{pid}}`

- Combine different options for tracing function in a process:

`dtrace -a -b {{buffer_size}} -f {{function}} -p {{pid}}`
