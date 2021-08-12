# quota

> Afișați utilizarea spațiului pe disc al utilizatorilor și limitele alocate.

- Afișează cote de disc în unități lizibile umane pentru utilizatorul curent:

`quota -s`

- ieșire verbose (de asemenea, afișează cote pentru sistemele de fișiere în cazul în care nu este alocat spațiu de stocare):

`quota -v`

- Ieşire silenţioasă (afişează doar cotele pentru sistemele de fişiere în care utilizarea depăşeşte cota):

`quota -q`

- Tipărirea cotelor pentru grupurile din care utilizatorul curent este membru:

`quota -g`

- Arată cote de disc pentru un alt utilizator:

`sudo quota -u {{username}}`
