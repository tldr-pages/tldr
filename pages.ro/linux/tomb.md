# tomb

> Gestionați directoarele de stocare criptate care pot fi transportate și ascunse în siguranță într-un sistem de fișiere.
> Mai multe informaţii: <https://www.dyne.org/software/tomb/>

- Creați un mormânt nou cu o dimensiune inițială de 100MB:

`tomb dig -s {{100}} {{encrypted_directory.tomb}}`

- Creați un nou fișier cheie care poate fi folosit pentru a bloca un mormânt; utilizatorul va fi solicitat pentru o parolă pentru cheie:

`tomb forge {{encrypted_directory.tomb.key}}`

- Creați cu forța o nouă cheie, chiar dacă mormântul nu permite forjarea cheilor (datorită schimbului):

`tomb forge {{encrypted_directory.tomb.key}} -f`

- Initializati si incuiati un mormant gol folosind o cheie facuta cu `falsificare`:

`tomb lock {{encrypted_directory.tomb}} -k {{encrypted_directory.tomb.key}}`

- Montați un mormânt (implicit în `/media`) folosind cheia sa, făcându-l utilizabil ca director obișnuit al sistemului de fișiere:

`tomb open {{encrypted_directory.tomb}} -k {{encrypted_directory.tomb.key}}`

- Închideți un mormânt (nu reușește dacă mormântul este folosit de un proces):

`tomb close {{encrypted_directory.tomb}}`

- Închideți cu forța toate mormintele deschise, omorând orice aplicație care le utilizează:

`tomb slam all`

- Listează toate mormintele deschise:

`tomb list`
