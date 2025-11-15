# msg

> Wyślij wiadomość do wybranego użytnownika lub sesji.
> Więcej informacji: <https://learn.microsoft.com/windows-server/administration/windows-commands/msg>.

- Wysyła wiadomość do użytkownika lub sesji:

`msg {{nazwa_użytkownika|nazwa_sesji|identyfikator_sesji}} {{wiadomość}}`

- Wyślij wiadomość ze standardowego wejścia:

`echo "{{wiadomość}}" | msg {{nazwa_użytkownika|nazwa_sesji|identyfikator_sesji}}`

- Wyślij wiadomość to zdalnej maszyny:

`msg /server:{{nazwa_serwera}} {{nazwa_użytkownika|nazwa_sesji|identyfikator_sesji}}`

- Wyślij wiadomość do wszystkich użytkowników aktualnej maszyny:

`msg *`

- Wyślij wiadomość z opóźnieniem:

`msg /time:{{seconds}}`
