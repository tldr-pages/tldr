# npm profile

> Управлять профилем npm и связанными настройками.
> Примечание: эта команда не поддерживает рабочие области.
> Больше информации: <https://docs.npmjs.com/cli/npm-profile/>.

- Показать данные профиля npm:

`npm profile get`

- Получить значение конкретного свойства профиля:

`npm profile get {{свойство}}`

- Установить или обновить свойство профиля:

`npm profile set {{свойство}} {{значение}}`

- Установить публичный адрес электронной почты:

`npm profile set email {{email}}`

- Установить публичное имя:

`npm profile set fullname {{имя}}`

- Установить новый пароль в интерактивном режиме:

`npm profile set password`

- Включить двухфакторную аутентификацию (2FA) (по умолчанию `auth-and-writes`):

`npm profile enable-2fa {{auth-only|auth-and-writes}}`

- Отключить двухфакторную аутентификацию (2FA):

`npm profile disable-2fa`
