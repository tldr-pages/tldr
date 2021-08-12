# z

> Urmăriți directoarele cele mai utilizate (după frecență) și permite navigarea rapidă la ele folosind modele de șir sau expresii regulate.
> Mai multe informaţii: <https://github.com/rupa/z>

- Du-te la un director care conține „foo” în numele:

`z {{foo}}`

- Du-te la un director care conține „foo” și apoi „bar”:

`z {{foo}} {{bar}}`

- Accesați cel mai bine clasat director care se potrivește cu „foo”:

`z -r {{foo}}`

- Accesați cel mai recent accesat director care se potrivește cu „foo”:

`z -t {{foo}}`

- Listează toate directoarele din baza de date a lui `z` care se potrivesc cu „foo”:

`z -l {{foo}}`

- Elimină directorul curent din baza de date a lui `z`:

`z -x .`

- Restricționați potriviri la subdirectoarele directorului curent:

`z -c {{foo}}`
