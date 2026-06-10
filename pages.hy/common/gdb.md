# գդբ

> GNU վրիպազերծիչ:.
> Լրացուցիչ տեղեկություններ. <https://sourceware.org/gdb/current/onlinedocs/gdb#Invocation>:.

- Վրիպազերծել գործարկվողը.:

`gdb {{path/to/executable}}`

- Կցեք գործընթաց `gdb`-ին.:

`gdb {{[-p|--pid]}} {{process_id}}`

- Վրիպազերծել հիմնական ֆայլով.:

`gdb {{[-c|--core]}} {{path/to/core}} {{path/to/executable}}`

- Գործարկեք տրված GDB հրամանները մեկնարկից.:

`gdb {{[-ex|--eval-command]}} "{{commands}}" {{path/to/executable}}`

- Սկսեք `gdb`-ը և արգումենտներ փոխանցեք գործարկվողին.:

`gdb --args {{path/to/executable}} {{argument1 argument2 ...}}`

- Բաց թողեք `debuginfod`-ը և էջադրման հուշումները, այնուհետև տպեք հետագիծը՝:

`gdb {{[-c|--core]}} {{path/to/core}} {{path/to/executable}} -iex 'set debuginfod enabled on' -iex 'set pagination off' -ex bt`
