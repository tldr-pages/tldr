# fakedata

> Generați date false utilizând o mare varietate de generatoare.
> Mai multe informaţii: <https://github.com/lucapette/fakedata>

- Listează toate generatoarele valide:

`fakedata --generators`

- Generarea datelor utilizând unul sau mai multe generatoare:

`fakedata {{generator1}} {{generator2}}`

- Generarea datelor cu un format specific de ieșire:

`fakedata --format {{csv|tab|sql}} {{generator}}`

- Generează un anumit număr de elemente de date (valori implicite la 10):

`fakedata --limit {{n}} {{generator}}`

- Generarea datelor utilizând un șablon de ieșire personalizat (prima literă a numelor generatorului trebuie să fie majuscule):

`echo "{{\{\{Generator\}\}}}" | fakedata`
