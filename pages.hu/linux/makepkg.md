# makepkg

> Létrehoz egy olyan csomagot, amely a `pacman` címmel használható. Alapértelmezés szerint az aktuális munkakönyvtárban lévő `PKGBUILD` fájlt használja. További információ: <https://man.archlinux.org/man/makepkg.8>.

- Csomag készítése:

`makepkg`

- Csomag készítése és függőségeinek telepítése:

`makepkg --syncdeps`

- Csomag készítése, függőségeinek telepítése, majd telepítése a rendszerbe:

`makepkg --syncdeps --install`

- Csomag készítése, de a forrás hash-ellenőrzés kihagyása:

`makepkg --skipchecksums`

- Sikeres összeállítás után a munkakönyvtárak kitakarítása:

`makepkg --clean`

- A források hash-jainak ellenőrzése:

`makepkg --verifysource`

- A forrásinformációk generálása és mentése a `.SRCINFO`:

`makepkg --printsrcinfo > .SRCINFO`
