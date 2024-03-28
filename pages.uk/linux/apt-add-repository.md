# apt-add-repository

> Керує взаємодією з репозиторіями `apt`.
> Більше інформації: <https://manpages.debian.org/latest/software-properties-common/apt-add-repository.1.html>.

- Додайте новий репозиторій `apt`:

`apt-add-repository {{репозиторій}}`

- Видалити репозиторій `apt`:

`apt-add-repository --remove {{репозиторій}}`

- Оновити кеш пакетів після додавання репозиторію:

`apt-add-repository --update {{репозиторій}}`

- Увімкнути вихідні пакети:

`apt-add-repository --enable-source {{репозиторій}}`
