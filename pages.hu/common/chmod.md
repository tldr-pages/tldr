# chmod

> Egy fájl vagy könyvtár hozzáférési jogosultságainak módosítása. További információ: <https://www.gnu.org/software/coreutils/chmod>.

- Adja meg a fájl tulajdonosa \[u\]ser számára az e\[x\]ecute jogát:

`chmod u+x {{path/to/file}}`

- Adja meg az \[u\]ser számára a \[r\]ead és \[w\]rite jogokat egy fájlhoz/könyvtárhoz:

`chmod u+rw {{path/to/file_or_directory}}`

- Távolítsa el az e\[x\]ecutable jogokat a \[g\]csoporttól:

`chmod g-x {{path/to/file}}`

- Adjon \[a\]ll felhasználónak \[r\]ead és e\[x\]ecute jogokat:

`chmod a+rx {{path/to/file}}`

- Adjon \[o\]thers (a fájl tulajdonosának csoportján kívüli felhasználóknak) ugyanazokat a jogokat, mint a \[g\]csoportnak:

`chmod o=g {{path/to/file}}`

- Minden jog megvonása a \[o\]thers-től:

`chmod o= {{path/to/file}}`

- A jogosultságok rekurzív módon történő módosítása, amely a \[g\]csoportnak és \[o\]thers-nek \[w\]rite képességet ad:

`chmod -R g+w,o+w {{path/to/directory}}`

- Rekurzív módon \[a\]ll felhasználónak \[r\]ead jogokat ad a fájlokra és e\[X\]ecute jogokat a könyvtáron belüli alkönyvtárakra:

`chmod -R a+rX {{path/to/directory}}`
