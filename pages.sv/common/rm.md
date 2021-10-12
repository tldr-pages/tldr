# rm

> Ta bort filer eller mappar.
> Mer information: <https://www.gnu.org/software/coreutils/rm>.

- Ta bort filer från ett godtyckligt ställe:

`rm {{path/to/file}} {{path/to/another/file}}`

- Rekursivt ta bort en mapp och dess undermappar:

`rm -r {{path/to/directory}}`

- Tvinga borttagning av en mapp utan att konfirmera eller visa error meddelanden:

`rm -rf {{path/to/directory}}`

- Interaktivt ta bort flera filer, genom att fråga om borttagning för varje fil:

`rm -i {{file(s)}}`

- Ta bort filer och visa ett meddelande för varje borttagning:

`rm -v {{path/to/directory/*}}`
