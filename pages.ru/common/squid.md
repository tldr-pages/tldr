# squid

> Кэшировать и перенаправлять HTTP-запросы через прокси-сервер.
> Больше информации: <https://manned.org/squid>.

- Запустить Squid в фоновом режиме:

`sudo squid`

- Запустить Squid на переднем плане (не в фоновом режиме):

`sudo squid -N`

- Запустить Squid с указанным файлом конфигурации:

`sudo squid -f {{путь/к/squid.conf}}`

- Проверить файл конфигурации на наличие ошибок:

`sudo squid -k parse`

- Перезагрузить файл конфигурации:

`sudo squid -k reconfigure`

- Корректно остановить Squid:

`sudo squid -k shutdown`

- Выполнить ротацию файлов журнала:

`sudo squid -k rotate`
