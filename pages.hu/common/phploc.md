# phploc

> Egy eszköz egy PHP projekt méretének gyors mérésére és szerkezetének elemzésére. További információ: <https://github.com/sebastianbergmann/phploc>.

- Egy könyvtár elemzése és az eredmény kinyomtatása:

`phploc {{path/to/directory}}`

- Csak bizonyos fájlok felvétele egy vesszővel elválasztott listából (a globok megengedettek):

`phploc {{path/to/directory}} --names {{files}}`

- Bizonyos fájlok kizárása egy vesszővel elválasztott listából (globs engedélyezett):

`phploc {{path/to/directory}} --names-exclude {{files}}`

- Egy adott könyvtár kizárása az elemzésből:

`phploc {{path/to/directory}} --exclude {{path/to/exclude_directory}}`

- Naplózza az eredményeket egy adott CSV-fájlba:

`phploc {{path/to/directory}} --log-csv {{path/to/file}}`

- Naplózza az eredményeket egy adott XML-fájlba:

`phploc {{path/to/directory}} --log-xml {{path/to/file}}`

- PHPUnit teszteset osztályok és tesztmódszerek számolása:

`phploc {{path/to/directory}} --count-tests`
