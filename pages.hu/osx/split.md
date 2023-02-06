# split

> Egy fájl darabokra osztása. További információ: <https://ss64.com/osx/split.html>.

- Egy fájl felosztása, minden felosztás 10 sorból áll (kivéve az utolsó felosztást):

`split -l {{10}} {{filename}}`

- Egy fájl felosztása reguláris kifejezéssel. A megfelelő sor lesz a következő kimeneti fájl első sora:

`split -p {{cat|^[dh]og}} {{filename}}`

- Egy fájl felosztása 512 bájttal minden felosztásban (kivéve az utolsó felosztást; használja az 512k-t a kilobájtokra és az 512m-t a megabájtokra):

`split -b {{512}} {{filename}}`
