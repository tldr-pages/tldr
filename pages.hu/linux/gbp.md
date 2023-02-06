# gbp

> A Debian csomagkészítő rendszer és a Git integrálására szolgáló rendszer. További információ: <http://honk.sigxcpu.org/projects/git-buildpackage/manual-html/gbp.html>.

- Egy meglévő Debian csomag átalakítása gbp-re:

`gbp import-dsc {{path/to/package.dsc}}`

- Építse a csomagot az aktuális könyvtárban az alapértelmezett építőprogrammal (`debuild`):

`gbp buildpackage -jauto -us -uc`

- Csomag építése a `pbuilder` környezetben a Debian Bullseye számára:

`DIST={{bullseye}} ARCH={{amd64}} gbp buildpackage -jauto -us -uc --git-builder={{git-pbuilder}}`

- Adja meg, hogy egy csomag csak forráskódra legyen feltöltve a `.changes` fájlban (lásd https://wiki.debian.org/SourceOnlyUpload):

`gbp buildpackage -jauto -us -uc --changes-options={{-S}}`

- Új upstream kiadás importálása:

`gbp import-orig --pristine-tar {{path/to/package.tar.gz}}`
