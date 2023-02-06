# whereis

> Egy parancs bináris, forrás- és kézikönyvoldali fájljainak keresése. További információ: <https://manned.org/whereis>.

- Az ssh bináris, forrás és man oldalak keresése:

`whereis {{ssh}}`

- Az ls bináris és man oldalak keresése:

`whereis -bm {{ls}}`

- A gcc forrás és man oldalak keresése a Git-hez:

`whereis -s {{gcc}} -m {{git}}`

- A gcc bináris állományainak keresése csak a `/usr/bin/` oldalon:

`whereis -b -B {{/usr/bin/}} -f {{gcc}}`

- Szokatlan binárisok keresése (olyanok, amelyeknek egynél több vagy kevesebb bináris van a rendszerben):

`whereis -u *`

- (olyan binárisok, amelyeknek egynél több vagy kevesebb kézikönyv van telepítve):

`whereis -u -m *`
