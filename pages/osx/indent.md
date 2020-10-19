# indent

> Change the appearance of a C/C++ program by inserting or deleting whitespace.
> More information: <https://www.freebsd.org/cgi/man.cgi?query=indent>.

- Format C/C++ source according to the Berkeley style:

`indent {{path/to/source.c}} {{path/to/indented_source.c}} -nbad -nbap -bc -br -c33 -cd33 -cdb -ce -ci4 -cli0 -di16 -fc1 -fcb -i4 -ip -l75 -lp -npcs -nprs -psl -sc -nsob -ts8`

- Format C/C++ source according to the style of Kernigan & Ritchie (K&R):

`indent {{path/to/source.c}} {{path/to/indented_source.c}} -nbad -bap -nbc -br -c33 -cd33 -ncdb -ce -ci4 -cli0 -cs -d0 -di1 -nfc1 -nfcb -i4 -nip -l75 -lp -npcs -nprs -npsl -nsc -nsob`
