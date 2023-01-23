# yes

> Ismételten kiad valamit. Ezt a parancsot általában arra használják, hogy a telepítő parancsok (például az apt-get) minden kérésre igennel válaszoljanak. További információ: <https://www.gnu.org/software/coreutils/yes>.

- Ismételten kiadja az "üzenetet":

`yes {{message}}`

- Ismételt "y" kimenet:

`yes`

- Elfogad mindent, amit a `apt-get` parancs kérdez:

`yes | sudo apt-get install {{program}}`
