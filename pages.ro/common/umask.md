# umask

> Gestionați permisiunile de citire/scriere/executare care sunt mascate (adică restricționate) pentru fișierele nou create de utilizator.

- Afișează masca curentă în notație octală:

`umask`

- Afișați masca curentă în modul simbolic (ușor de citit de om):

`umask -S`

- Schimbați masca simbolic pentru a permite permisiunea de citire pentru toți utilizatorii (restul biților de mască sunt neschimbați):

`umask {{a+r}}`

- Setați masca (folosind octal) pentru a restricționa nicio permisiune pentru proprietarul fișierului și restricționați toate permisiunile pentru toți ceilalți:

`umask {{077}}`
