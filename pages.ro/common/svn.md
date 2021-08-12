# svn

> Subversiune instrument client linie de comandă.
> Mai multe informaţii: <https://subversion.apache.org>

- Check out o copie de lucru dintr-un depozit:

`svn co {{url/to/repository}}`

- Aduceți modificările din depozit în copia de lucru:

`svn up`

- Puneți fișierele și directoarele sub controlul versiunii, programându-le pentru adăugarea la depozit. Acestea vor fi adăugate în următoarea angajare:

`svn add {{PATH}}`

- Trimiteți modificări din copia dvs. de lucru în depozit:

`svn ci -m {{commit_log_message}} [{{PATH}}]`

- Afișează modificările din ultimele 10 revizuiri, afișând fișiere modificate pentru fiecare revizuire:

`svn log -vl {{10}}`

- Arată ajutor detaliat:

`svn help`
