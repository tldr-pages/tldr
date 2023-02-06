# split

> Egy fájl darabokra osztása. További információ: <https://www.gnu.org/software/coreutils/split>.

- Egy fájl felosztása, minden felosztás 10 sorból áll (kivéve az utolsó felosztást):

`split -l {{10}} {{path/to/file}}`

- Egy fájl felosztása 5 fájlra. A fájl felosztása úgy történik, hogy mindegyik felosztás azonos méretű (kivéve az utolsó felosztást):

`split -n {{5}} {{path/to/file}}`

- A fájl felosztása úgy, hogy minden felosztás 512 bájtot tartalmaz (kivéve az utolsó felosztást; a kilobájt esetében 512k, a megabájt esetében 512m):

`split -b {{512}} {{path/to/file}}`

- A fájl felosztása minden egyes felosztásban legfeljebb 512 bájttal, sorok megszakítása nélkül:

`split -C {{512}} {{path/to/file}}`
