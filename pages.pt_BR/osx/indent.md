# indent

> Altera a aparência de um programa C/C++ inserindo ou excluindo espaços em branco.
> Mais informações: <https://www.freebsd.org/cgi/man.cgi?query=indent>.

- Formata código fonte C/C++ de acordo com o estilo Berkeley:

`indent {{caminho/para/fonte.c}} {{caminho/para/fonte_identado.c}} -nbad -nbap -bc -br -c33 -cd33 -cdb -ce -ci4 -cli0 -di16 -fc1 -fcb -i4 -ip -l75 -lp -npcs -nprs -psl -sc -nsob -ts8`

- Formata código fonte C/C++ de acordo com o estilo Kernighan & Ritchie (K&R):

`indent {{caminho/para/fonte.c}} {{caminho/para/fonte_identado.c}} -nbad -bap -nbc -br -c33 -cd33 -ncdb -ce -ci4 -cli0 -cs -d0 -di1 -nfc1 -nfcb -i4 -nip -l75 -lp -npcs -nprs -npsl -nsc -nsob`
