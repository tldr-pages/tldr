# coreutils

> Uutils coreutils is a cross-platform reimplementation of the GNU coreutils in Rust Language.
> Uutils includes a multi-call binary from which the utils can be invoked. This reduces the binary size of the binary and can be useful for portability.
> More information: <https://uutils.github.io/coreutils/docs/multicall.html>.

- The first argument of the multi-call binary is the util to run, after which the regular arguments to the util can be passed:

`coreutils {{util}} {{util_options}}`

- It can be execeuted as following example of list command(ls):

`coreutils ls -l`

- The --help flag will print a list of available utils for a command:

`coreutils ls --help`
