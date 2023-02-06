# indent

> A C/C++ program megjelenésének megváltoztatása szóközök beillesztésével vagy törlésével. További információ: <https://www.freebsd.org/cgi/man.cgi?query=indent>.

- A C/C++ forráskód formázása a Berkeley stílus szerint:

`indent {{path/to/source.c}} {{path/to/indented_source.c}} -nbad -nbap -bc -br -c33 -cd33 -cdb -ce -ci4 -cli0 -di16 -fc1 -fcb -i4 -ip -l75 -lp -npcs -nprs -psl -sc -nsob -ts8`

- C/C++ forrás formázása a Kernighan & Ritchie (K&R) stílusa szerint:

`indent {{path/to/source.c}} {{path/to/indented_source.c}} -nbad -bap -nbc -br -c33 -cd33 -ncdb -ce -ci4 -cli0 -cs -d0 -di1 -nfc1 -nfcb -i4 -nip -l75 -lp -npcs -nprs -npsl -nsc -nsob`
