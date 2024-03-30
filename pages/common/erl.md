# erl

> Run and manage programs in the Erlang programming language.
> More information: <https://www.erlang.org>.

- Compile and run sequential Erlang program as a common script and then exit:

`erlc {{path/to/file1 path/to/file2 ...}} && erl -noshell '{{mymodule:myfunction(arguments)}}, init:stop().'`

- Connect to a running Erlang node:

`erl -remsh {{nodename}}@{{hostname}} -sname {{custom_shortname}} -hidden -setcookie {{cookie_of_remote_node}}`

- Tell the Erlang shell to load modules from a directory:

`erl -pa {{path/to/directory_with_beam_files}}`
