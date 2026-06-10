# in-toto-record

> Ստեղծեք ստորագրված հղման մետատվյալների ֆայլ՝ մատակարարման շղթայի քայլերի համար ապացույցներ ապահովելու համար:.
> Լրացուցիչ տեղեկություններ. <https://in-toto.readthedocs.io/en/latest/command-line-tools/in-toto-record.html>:.

- Սկսեք գրառումը (ստեղծում է նախնական հղման ֆայլ).:

`in-toto-record start {{[-n|--step-name]}} {{path/to/edit_file1 path/to/edit_file2 ...}} --signing-key {{path/to/key_file}} {{[-m|--materials]}} {{.}}`

- Դադարեցրեք գրառումը (ակնկալում է նախնական հղման ֆայլ).:

`in-toto-record stop {{[-n|--step-name]}} {{path/to/edit_file1 path/to/edit_file2 ...}} --signing-key {{path/to/key_file}} {{[-p|--products]}} {{.}}`
