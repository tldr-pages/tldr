# systemd-run

> Uruchamiaj programy w przejściowych jednostkach zakresu, jednostkach usługowych lub jednostkach usługowych uruchamianych przez ścieżkę, gniazdo lub timer.
> Więcej informacji: <https://www.freedesktop.org/software/systemd/man/systemd-run.html>.

- Uruchom przejściową usługę:

`sudo systemd-run {{komenda}} {{argument1 argument2 ...}}`

- Uruchom przejściową usługę pod menedżerem usług aktualnego użytkownika (bez uprawnień):

`systemd-run --user {{komenda}} {{argument1 argument2 ...}}`

- Uruchom przejściową usługę z podaną nazwą jednostki i opisem:

`sudo systemd-run --unit={{nazwa}} --description={{string}} {{komenda}} {{argument1 argument2 ...}}`

- Uruchom przejściową usługę, która nie jest czyszczona po jej zakończeniu z podaną zmienną środowiskową:

`sudo systemd-run --remain-after-exit --set-env={{nazwa}}={{wartość}} {{komenda}} {{argument1 argument2 ...}}`

- Uruchom przejściowy timer, który okresowo uruchamia swoją przejściową usługę (zobacz `man systemd.time`, aby zapoznać się z formatem wydarzeń kalendarza):

`sudo systemd-run --on-calendar={{wydarzenie_kalendarza}} {{komenda}} {{argument1 argument2 ...}}`

- Udostępnij terminal programowi (umożliwiając interaktywne wejście/wyjście) i zapewnij, że szczegóły wykonania pozostaną po zakończeniu programu:

`systemd-run --remain-after-exit --pty {{komenda}}`

- Ustaw właściwości (np. CPUQuota, MemoryMax) procesu i poczekaj, aż się zakończy:

`systemd-run --property MemoryMax={{pamięć_w_bajtach}} --property CPUQuota={{procent_czasu_CPU}}% --wait {{komenda}}`

- Użyj programu w potoku powłoki:

`{{komenda1}} | systemd-run --pipe {{komenda2}} | {{komenda3}}`
