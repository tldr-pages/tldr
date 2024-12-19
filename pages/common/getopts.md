# getopts

> Parse shell options from arguments.
> This command does not support longform options and thus using `getopt` is recommended instead.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#index-getopts>.

- Check if an option is set:

`getopts {{x}} {{opt}}; echo $opt`

- Set an option to require an argument and check said argument:

`getopts {{x}}: {{opt}}; echo $OPTARG`

- Check for multiple options:

`while getopts {{xyz}} {{opt}}; do case $opt in x) echo x is set;; y) echo y is set;; z) echo z is set;; esac; done`

- Set `getopts` to silent mode and handle option errors:

`while getopts :{{x:}} {{opt}}; do case $opt in x) ;; :) echo "Argument required";; ?) echo "Invalid argument" esac;; done`

- Reset `getopts`:

`OPTIND=1`
