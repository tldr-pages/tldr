# pathchk

> Sprawdź poprawność oraz przenośność jednej lub większej ilości ścieżek.
> Więcej informacji: <https://www.gnu.org/software/coreutils/manual/html_node/pathchk-invocation.html>.

- Sprawdź ścieżki pod kątem poprawności w obecnym systemie:

`pathchk {{ścieżka1 ścieżka2 ...}}`

- Sprawdź ścieżki pod kątem poprawności w szerszym zakresie systemów zgodnych z POSIX:

`pathchk -p {{ścieżka1 ścieżka2 ...}}`

- Sprawdź ścieżki pod kątem poprawności we wszystkich systemach zgodnych z POSIX:

`pathchk {{[-p -P|--portability]}} {{ścieżka1 ścieżka2 ...}}`

- Sprawdź tylko pod kątem pustych ścieżek lub wiodących myślników (-):

`pathchk -P {{ścieżka1 ścieżka2 ...}}`
