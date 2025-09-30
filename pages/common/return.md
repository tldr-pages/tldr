# return

> Exit a function or a script if run with `source`.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#index-return>.

- Exit a function prematurely:

`{{func_name}}() { {{echo "This is reached"}}; return; {{echo "This is not"}}; }`

- Specify the function's return value:

`{{func_name}}() { return {{exit_code}}; }`
