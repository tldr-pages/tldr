# getopts

> Parse shell options from arguments.
> This command does not support longform options and thus using `getopt` is recommended instead.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#index-getopts>.

- Check if an option is the first set option in the current context:

`getopts {{x}} {{opt}}; echo ${{opt}}`

- Check if an option is set in a string (specified option must be the first element of the string):

`getopts {{x}} {{opt}} "{{string text}}"; echo ${{opt}}`

- Set an option to require an argument and print them:

`getopts {{x}}: {{opt}}; echo ${{opt}} $OPTARG`

- Check for multiple options:

`while getopts {{xyz}} {{opt}}; do case ${{opt}} in x) {{echo x is set}};; y) {{echo y is set}};; z) {{echo z is set}};; esac; done`

- Set `getopts` to silent mode and handle option errors:

`while getopts :{{x:}} {{opt}}; do case ${{opt}} in x) ;; :) {{echo "Argument required"}};; ?) {{echo "Invalid argument"}} esac;; done`

- Reset `getopts`:

`OPTIND=1`
