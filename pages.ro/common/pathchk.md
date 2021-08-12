# pathchk

> Verificați validitatea și portabilitatea unuia sau mai multor căi.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/pathchk>

- Verificați căile de valabilitate în sistemul curent:

`pathchk {{path1 path2 …}}`

- Verificați numele de căi pentru valabilitate pe o gamă mai largă de sisteme compatibile POSIX:

`pathchk -p {{path1 path2 …}}`

- Verificați numele de cai pentru valabilitate pe toate sistemele compatibile POSIX:

`pathchk --portability {{path1 path2 …}}`

- Verificați numai numele de cai goale sau liniuțele de conducere (-):

`pathchk -P {{path1 path2 …}}`
