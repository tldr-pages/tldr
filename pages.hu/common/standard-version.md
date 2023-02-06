# standard-version

> A SemVer és a Conventional Commits segítségével automatizálhatja a verziókezelést és a changelog generálást. További információ: <https://github.com/conventional-changelog/standard-version>.

- A changelog fájl frissítése és a kiadás megjelölése:

`standard-version`

- Jelöljön meg egy kiadást anélkül, hogy a verziót feldobná:

`standard-version --first-release`

- A changelog frissítése és egy alfa kiadás megjelölése:

`standard-version --prerelease alpha`

- A changelog frissítése és egy adott kiadványtípus megjelölése:

`standard-version --release-as {{major|minor|patch}}`

- Kiadás címkézése, megakadályozva a horgok ellenőrzését a commit lépés során:

`standard-version --no-verify`

- Kiadás címkézése, amely az összes lépcsőzetes módosítást commitolja, nem csak a `standard-version` által érintett fájlokat:

`standard-version --commit-all`

- Egy adott changelog fájl frissítése és egy kiadás megjelölése:

`standard-version --infile {{path/to/file.md}}`

- Megjeleníti a kiadást, amelyet ezek végrehajtása nélkül hajtanának végre:

`standard-version --dry-run`
