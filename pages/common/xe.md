# xe

> Execute a command once for each line piped from another command or file.
> More information: <https://github.com/leahneukirchen/xe>.

- Run a command once for each line of input data as arguments:

`{{arguments_source}} | xe {{command}}`

- Execute the commands, replacing any occurrence of the placeholder (marked as `{}`) with the input line:

`{{arguments_source}} | xe {{command}} {} {{optional_extra_arguments}}`

- Execute a shellscript, joining every `N` lines into a single call:

`echo -e 'a\nb' | xe -N{{2}} -s 'echo $2 $1'`

- Delete all files with a `.backup` extension:

`find . -name {{'*.backup'}} | xe rm -v`

- Run up to `max-jobs` processes in parallel; the default is 1. If `max-jobs` is 0, xe will run as many processes as cpu cores:

`{{arguments_source}} | xe -j {{max-jobs}} {{command}}`
