# yacc

Generate a LALR parser (in C) with a given formal grammar specification file.

More information on `yacc` and LALR parsers:

`yacc`: https://en.wikipedia.org/wiki/Yacc\
LALR parsers: https://en.wikipedia.org/wiki/LALR_parser 

Examples (given a formal grammar specification file grammar.y):


Create a file `y.tab.c` contatining the parser code in C, and `y.tab.h`, which contains all neccecary constant declarations for values specified in the grammar file. (This constant declarations file is created only when the `-d` flag is used):

- `yacc -d grammar.y`
    
 Does the same as above, but generates a report file (`y.output`) on the grammar containing a simple description and any conflicts / invalid features of the grammar:

- `yacc -d grammar.y -v`

Same as above, but will replace the 'y' prepending the output files with 'prefix' instead (a.k.a, generate `prefix.tab.c` and `prefix.tab.h`):

- `yacc -d grammar.y -v -b prefix`

    