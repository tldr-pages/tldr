# git format-patch

> .patch fájlok előkészítése. Hasznos, ha a commitokat máshová küldjük e-mailben. Lásd még: `git am`, amely képes alkalmazni a generált .patch fájlokat. További információ: <https://git-scm.com/docs/git-format-patch>.

- Hozzon létre egy automatikusan elnevezett `.patch` fájlt az összes még el nem küldött commithoz:

`git format-patch {{origin}}`

- Írjon egy `.patch` fájlt az összes, 2 revízió közötti commithoz a `stdout` címre:

`git format-patch {{revision_1}}..{{revision_2}}`

- Írjon egy `.patch` fájlt a 3 legutóbbi commithoz:

`git format-patch -{{3}}`
