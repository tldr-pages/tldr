#միզ

> Միացնել `stdin` խողովակներին:.
> Տես նաև՝ `tee`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/pee>:.

- Գործարկեք յուրաքանչյուր հրաման՝ յուրաքանչյուրին տրամադրելով `stdin`-ի հստակ պատճենը՝:

`pee {{command1 command2 ...}}`

- Գրեք `stdin`-ի պատճենը `stdout`-ին (ինչպես `tee`):

`pee cat {{command1 command2 ...}}`

- Անմիջապես դադարեցրեք SIGPIPE-ների վրա և գրեք սխալներ.:

`pee --no-ignore-sigpipe --no-ignore-write-errors {{command1 command2 ...}}`
