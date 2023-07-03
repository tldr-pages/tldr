# yacc

> Generate a LALR parser (in C) with a given formal grammar specification file.
> See also: `bison`.
> More information: <https://en.wikipedia.org/wiki/Yacc>.

- Create a file y.tab.c containing the parser code in C, and y.tab.h, which contains all necessary constant declarations for values specified in the grammar file. (This constant declarations file is created only when the -d flag is used):

`yacc -d {{grammar}}.y`

- Generate the same as above, but also generate report file (`y.output`) on the grammar containing a simple description and any conflicts / invalid features of the grammar:

`yacc -d {{grammar}}.y -v`

- Generate the same as above, but replace the 'y' prepending the output files with '{{prefix}}' instead (a.k.a, generate `{{prefix}}.tab.c` and `{{prefix}}.tab.h`):

`yacc -d grammar.y -v -b {{prefix}}`
