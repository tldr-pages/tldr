# erl

> Rulați și gestionați programe în limbajul de programare Erlang.
> Mai multe informaţii: <https://www.erlang.org>

- Compilați și executați programul secvențial Erlang ca un script comun și apoi ieșiți:

`erlc {{files}} && erl -noshell '{{mymodule:myfunction(arguments)}}, init:stop().'`

- Conectați-vă la un nod Erlang care rulează:

`erl -remsh {{nodename}}@{{hostname}} -sname {{custom_shortname}} -hidden -setcookie {{cookie_of_remote_node}}`

- Spune-i shell-ului Erlang să încarce module dintr-un director:

`erl -pa {{directory_with_beam_files}}`
