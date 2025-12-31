# dnf install

> Установка пакетов в дистрибутивах на базе Red Hat.
> Больше информации: <https://dnf.readthedocs.io/en/latest/command_ref.html#install-examples>.

- Установить пакеты по имени:

`sudo dnf {{[in|install]}} {{пакет1 пакет2 ...}}`

- Установить пакет из локального файла:

`sudo dnf {{[in|install]}} {{путь/к/файлу}}`

- Установить пакет из интернета:

`sudo dnf {{[in|install]}} {{https://example.com/package.rpm}}`

- Добавить репозитории Extra Packages for Enterprise Linux (EPEL):

`sudo dnf {{[in|install]}} https://dl.fedoraproject.org/pub/epel/epel-release-latest-{{10}}.noarch.rpm`

- Добавить RPM-репозиторий Remi:

`sudo dnf {{[in|install]}} https://rpms.remirepo.net/enterprise/remi-release-{{8}}.rpm`
