# jdupes

> Un căutător de fișiere duplicate puternic și o furcă îmbunătățită de fdupes.
> Mai multe informaţii: <https://github.com/jbruchon/jdupes>

- Caută într-un singur director:

`jdupes {{directory}}`

- Caută în mai multe directoare:

`jdupes {{directory1}} {{directory2}}`

- Caută în toate directoarele recursiv:

`jdupes --recurse {{directory}}`

- Caută în directorul recursiv și lăsați utilizatorul să aleagă fișiere pentru a păstra:

`jdupes --delete --recurse {{directory}}`

- Căutați mai multe directoare și urmați subdirectores sub directory2, nu directory1:

`jdupes {{directory1}} --recurse: {{directory2}}`

- Căutați mai multe directoare și păstrați ordinea directorului în rezultat:

`jdupes -O {{directory1}} {{directory2}} {{directory3}}`
