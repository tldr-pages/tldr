# erl

> Esegui e gestisci programmi nel linguaggio di programmazione Erlang.
> Maggiori informazioni: <https://erlang.org/documentation/doc-16.0/erts-16.0/doc/html/erl_cmd.html>.

- Compila ed esegui un programma Erlang sequenziale come un comune script e poi esci:

`erlc {{file}} && erl -noshell '{{modulo:funzione(argomenti)}}, init:stop().'`

- Connetti ad un nodo Erlang in esecuzione:

`erl -remsh {{nome_nodo}}@{{hostname}} -sname {{soprannome}} -hidden -setcookie {{cookie_nodo_remoto}}`

- Fai caricare alla shell Erlang dei moduli da una directory:

`erl -pa {{directory_con_file_beam}}`
