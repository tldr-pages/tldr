# chmod

> Schimbă permisiunile de acces ale unui fișier sau folder.
> Mai multe informații: <https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html>.

- Acordă [u]tilizatorului proprietar al fișierului dreptul de a-l e[x]ecuta:

`chmod u+x {{cale/către/fișier}}`

- Acordă [u]tilizatorului dreptul de a [r]ealiza citire și [w]riere asupra unui fișier/folder:

`chmod u+rw {{cale/către/fișier_sau_folder}}`

- Elimină dreptul de e[x]ecuție al [g]rupului:

`chmod g-x {{cale/către/fișier}}`

- Acordă tuturor utilizatorilor ([a]ll) dreptul de [r]ealizare citire și e[x]ecuție:

`chmod a+rx {{cale/către/fișier}}`

- Acordă [o]ricui (utilizatorilor din afara grupului proprietar) aceleași drepturi ca [g]rupul:

`chmod o=g {{cale/către/fișier}}`

- Elimină toate drepturile pentru [o]ricine:

`chmod o= {{cale/către/fișier}}`

- Schimbă recursiv permisiunile, acordând [g]rupului și c[o]mun dreptul de a scrie ([w]):

`chmod {{[-R|--recursive]}} g+w,o+w {{cale/către/folder}}`

- Acordă recursiv tuturor utilizatorilor ([a]ll) drept de [r]eaplicare. Acordă, de asemenea, drepturi de e[X]ecuție fișierelor care au cel puțin un drept de execuție și tuturor sub-folderelor:

`chmod {{[-R|--recursive]}} a+rX {{cale/către/folder}}`
