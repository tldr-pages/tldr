# LOADFIX

> Reduce available conventional memory for old programs (default: 64KB).
> More information: <https://www.dosbox.com/wiki/LOADFIX>.

- Start a program with 64KB allocated memory:

`LOADFIX {{program}}`

- Load with custom KB reduction (1-1024):

`LOADFIX -{{32}} {{mm2}}`

- Free all previously allocated memory:

`LOADFIX -f`
