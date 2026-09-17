# git annex

> Gestionează fișiere cu Git, fără a le include conținutul.
> Când un fișier este anexat, conținutul său este mutat într-un depozit cheie-valoare, și se creează un symlink care indică către conținut.
> Mai multe informații: <https://git-annex.branchable.com/git-annex/>.

- Inițializează un repo cu Git annex:

`git annex init`

- Adaugă un fișier:

`git annex add {{cale/către/fișier_sau_director}}`

- Afișează starea curentă a unui fișier sau director:

`git annex status {{cale/către/fișier_sau_director}}`

- Sincronizează un repository local cu unul la distanță:

`git annex {{la_distanță}}`

- Obține un fișier sau director:

`git annex get {{cale/către/fișier_sau_director}}`

- Afișează ajutorul:

`git annex help`
