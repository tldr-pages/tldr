# erl

> Programok futtatása és kezelése az Erlang programozási nyelven. További információ: <https://www.erlang.org>.

- Szekvenciális Erlang program fordítása és futtatása közös szkriptként, majd kilépés:

`erlc {{files}} && erl -noshell '{{mymodule:myfunction(arguments)}}, init:stop().'`

- Csatlakozás egy futó Erlang-csomóponthoz:

`erl -remsh {{nodename}}@{{hostname}} -sname {{custom_shortname}} -hidden -setcookie {{cookie_of_remote_node}}`

- Mondja meg az Erlang shellnek, hogy töltsön be modulokat egy könyvtárból:

`erl -pa {{directory_with_beam_files}}`
