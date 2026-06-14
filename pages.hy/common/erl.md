#երլ

> Գործարկել և կառավարել ծրագրերը Erlang ծրագրավորման լեզվով:.
> Լրացուցիչ տեղեկություններ. <https://erlang.org/documentation/doc-16.0/erts-16.0/doc/html/erl_cmd.html>:.

- Կազմեք և գործարկեք հաջորդական Erlang ծրագիրը որպես ընդհանուր սցենար և այնուհետև դուրս եկեք.:

`erlc {{path/to/file1 path/to/file2 ...}} && erl -noshell '{{mymodule:myfunction(arguments)}}, init:stop().'`

- Միացեք գործող Erlang հանգույցին.:

`erl -remsh {{nodename}}@{{hostname}} -sname {{custom_shortname}} -hidden -setcookie {{cookie_of_remote_node}}`

- Ասեք Erlang shell-ին, որ բեռնել մոդուլները գրացուցակից.:

`erl -pa {{path/to/directory_with_beam_files}}`
