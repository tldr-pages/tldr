# git am

> Foltfájlok alkalmazása. Hasznos, ha e-mailben kapja a commitokat. Lásd még: `git format-patch`, amely képes patch fájlokat generálni. További információ: <https://git-scm.com/docs/git-am>.

- Foltfájl alkalmazása:

`git am {{path/to/file.patch}}`

- Megszakítja a javítófájl alkalmazásának folyamatát:

`git am --abort`

- A javítófájl minél nagyobb részének alkalmazása, a sikertelen részek mentése a selejtfájlokba:

`git am --reject {{path/to/file.patch}}`
