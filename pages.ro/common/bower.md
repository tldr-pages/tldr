# bower

> Un manager de pachete optimizat pentru dezvoltarea web front-end.
> Un pachet poate fi un scurtcircuit de utilizator/repo GitHub, un punct final Git, un URL sau un pachet înregistrat.
> Mai multe informaţii: <https://bower.io/>

- Instalați dependențele unui proiect, listate în bower.json său:

`bower install`

- Instalați unul sau mai multe pachete în directorul bower_components:

`bower install {{package}} {{package}}`

- Dezinstalați pachetele local din directorul bower_components:

`bower uninstall {{package}} {{package}}`

- Lista pachetelor locale și posibile actualizări:

`bower list`

- Afișează informații de ajutor despre o comandă de bower:

`bower help {{command}}`

- Creați un fișier `bower.json` pentru pachetul dvs.:

`bower init`

- Instalați o versiune de dependență specifică și adăugați-o la `bower.json`:

`bower install {{local_name}}={{package}}#{{version}} --save`
