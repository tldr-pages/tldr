# node

> Platformă JavaScript pe partea serverului (Node.js).
> Mai multe informaţii: <https://nodejs.org>

- Rulați un fișier JavaScript:

`node {{path/to/file}}`

- Porniți un REPL (shell interactiv):

`node`

- Evaluați codul JavaScript trecându-l ca argument:

`node -e "{{code}}"`

- Evaluați și imprimați rezultatul, util pentru a vedea versiunile dependențelor nodului:

`node -p "{{process.versions}}"`

- Activați inspectorul, întreruperea executării până când un depanator este conectat odată ce codul sursă este complet analizat:

`node --no-lazy --inspect-brk {{path/to/file}}`
