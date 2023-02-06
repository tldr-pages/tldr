# rankmirrors

> A Pacman tükrök listájának rangsorolása kapcsolat és nyitási sebesség alapján. Az új tükörlistát a `stdout` címre írja. További információ: <https://wiki.archlinux.org/index.php/mirrors>.

- Tükörlista rangsorolása:

`rankmirrors {{/etc/pacman.d/mirrorlist}}`

- Csak egy adott számú, a rangsor élén álló szervert ad ki:

`rankmirrors -n {{number}} {{/etc/pacman.d/mirrorlist}}`

- Legyen bőbeszédű a tükörlista létrehozásakor:

`rankmirrors -v {{/etc/pacman.d/mirrorlist}}`

- Csak egy adott URL-t teszteljen:

`rankmirrors --url {{url}}`

- A teljes tükörlista helyett csak a válaszidőt adja ki:

`rankmirrors --times {{/etc/pacman.d/mirrorlist}}`
