# gitlab-ctl

> Управлять GitLab Omnibus.
> Больше информации: <https://docs.gitlab.com/omnibus/maintenance/>.

- Показать статус всех сервисов:

`sudo gitlab-ctl status`

- Показать статус конкретного сервиса:

`sudo gitlab-ctl status {{nginx}}`

- Перезапустить все сервисы:

`sudo gitlab-ctl restart`

- Перезапустить конкретный сервис:

`sudo gitlab-ctl restart {{nginx}}`

- Показать логи всех сервисов и продолжать чтение до нажатия `<Ctrl c>`:

`sudo gitlab-ctl tail`

- Показать логи конкретного сервиса:

`sudo gitlab-ctl tail {{nginx}}`

- Отправить сигнал `SIGKILL` конкретному сервису:

`sudo gitlab-ctl kill {{nginx}}`

- Перенастроить приложение:

`sudo gitlab-ctl reconfigure`
