# rm

> Ta bort filer eller mappar.
> Mer information: <https://www.gnu.org/software/coreutils/rm>.

- Ta bort filer från godtyckliga ställen:

`rm {{sökväg/till/fil}} {{sökväg/till/en/annan/fil}}`

- Rekursivt ta bort en mapp och dess undermappar:

`rm -r {{sökväg/till/mapp}}`

- Tvinga borttagning av en mapp utan att bekräfta eller visa felmeddelanden:

`rm -rf {{sökväg/till/mapp}}`

- Interaktivt ta bort flera filer, genom att fråga om borttagning för varje fil:

`rm -i {{fil(er)}}`

- Ta bort filer och visa ett meddelande för varje borttagning:

`rm -v {{sökväg/till/mapp/*}}`
