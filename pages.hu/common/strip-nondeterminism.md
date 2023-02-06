# strip-nondeterminism

> Eszköz a nem determinisztikus információk (pl. időbélyegek) eltávolítására a fájlokból. További információ: <https://salsa.debian.org/reproducible-builds/strip-nondeterminism>.

- Nemdeterminisztikus információk eltávolítása egy fájlból:

`strip-nondeterminism {{path/to/file}}`

- A nemdeterminisztikus információk eltávolítása egy fájlból kézzel, a fájltípus megadásával:

`strip-nondeterminism --type {{filetype}} {{path/to/file}}`

- Nemdeterminisztikus információk eltávolítása egy fájlból; az időbélyegek eltávolítása helyett a megadott UNIX időbélyegre állítsa be azokat:

`strip-nondeterminism --timestamp {{unix_timestamp}} {{path/to/file}}`
