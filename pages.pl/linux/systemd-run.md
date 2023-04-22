# systemd-run

> Uruchamiaj programy w jednostkach przejściowych.
> Więcej informacji: <https://manned.org/systemd-run>.

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
