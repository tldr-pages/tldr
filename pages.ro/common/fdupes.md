# fdupes

> Găsește fișiere duplicate într-un anumit set de directoare.
> Mai multe informaţii: <https://github.com/adrianlopezroche/fdupes>

- Caută într-un singur director:

`fdupes {{directory}}`

- Caută în mai multe directoare:

`fdupes {{directory1}} {{directory2}}`

- Caută într-un director recursiv:

`fdupes -r {{directory}}`

- Caută mai multe directoare, unul recursiv:

`fdupes {{directory1}} -R {{directory2}}`

- Căutați recursiv duplicate și afișați prompt interactiv pentru a alege pe care să le păstrați, ștergându-le pe celelalte:

`fdupes -rd {{directory}}`

- Căutați recursiv și ștergeți duplicate fără a solicita:

`fdupes -rdN {{directory}}`
