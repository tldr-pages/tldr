# git effort

> Afișați cantitatea de activitate a avut un fișier, afișând angajările per fișier și „zile active”, adică numărul total de zile care au contribuit la fișier.
> Parte din `git-extras`.
> Mai multe informaţii: <https://github.com/tj/git-extras/blob/master/Commands.md#git-effort>

- Afișează fiecare fișier în depozit, arătând angajările și zilele active:

`git effort`

- Afișează fișiere modificate de un anumit număr de angajări sau mai multe, afișând angajări și zile active:

`git effort --above {{5}}`

- Afișează fișiere modificate de un anumit autor, prezentând angajări și zile active:

`git effort -- --author="{{username}}"`

- Afișează fișiere modificate de la o anumită oră/dată, afișând angajări și zile active:

`git effort -- --since="{{last month}}"`

- Afișează numai fișierele sau directoarele specificate, afișând angajamente și zile active:

`git effort {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Afișați toate fișierele într-un anumit director, afișând angajări și zile active:

`git effort {{path/to/directory/*}}`
