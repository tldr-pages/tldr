# chmod

> Modificați permisiunile de acces ale unui fișier sau ale unui director.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/chmod>

- Dă [u] ser care deține un fișier dreptul de a e [x] ecute:

`chmod u+x {{file}}`

- Dă [u] drepturile ser [r] cap și [w] rit la un fișier/director:

`chmod u+rw {{file_or_directory}}`

- Eliminați e [x] drepturile ecutabile din [g] roup:

`chmod g-x {{file}}`

- Dă [a] ll utilizatorilor drepturi de [r] ead și e [x] ecute:

`chmod a+rx {{file}}`

- Dați [o] thers (nu în grupul proprietarului fișierului) aceleași drepturi ca și [g] roup:

`chmod o=g {{file}}`

- Eliminați toate drepturile de la [o] thers:

`chmod o= {{file}}`

- Modificarea permisiunilor recursiv oferind [g] roup și [o] thers capacitatea de a [w] rit:

`chmod -R g+w,o+w {{directory}}`
