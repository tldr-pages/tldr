# pamfunc

> Apply a simple arithmetic function to a Netpbm image.
> More information: <https://netpbm.sourceforge.net/doc/pamfunc.html>.

- Apply the specified arithmetic function with `n` as the second argument to each sample in the specified PAM image:

`pamfunc -{{multiplier|divisor|adder|subtractor|min|max}} {{n}} {{path/to/input.pam}} > {{path/to/output.pam}}`

- Apply the specified bit string function with `n` as the second argument to each sample in the specified PAM image:

`pamfunc -{{andmask|ormask|xormask|shiftleft|shiftright}} {{n}} {{path/to/input.pam}} > {{path/to/output.pam}}`
