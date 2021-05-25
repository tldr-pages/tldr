# atq

> Pokaż oczekujące zadania użytkownika wprowadzone wcześniej przez polecenia `at` lub `batch`.
> Więcej informacji: <https://man.archlinux.org/man/at.1>.

- Pokaż zaplanowane zadania:

`atq`

- Pokaż zadania z kolejki oznaczonej 'a' (kolejki mają jednoznakowe identyfikatory):

`atq -q {{a}}`

- Pokaż zadania wszystkich użytkowników (uruchom jako superużytkownik):

`sudo atq`
