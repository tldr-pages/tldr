# postfix

> Программа управления почтовым агентом (MTA) Postfix.
> Смотрите также: `dovecot`, агент доставки почты (MDA), который интегрируется с Postfix.
> Больше информации: <https://www.postfix.org/postfix.1.html>.

- Проверить конфигурацию:

`sudo postfix check`

- Проверить статус демона Postfix:

`sudo postfix status`

- Запустить Postfix:

`sudo postfix start`

- Корректно остановить Postfix:

`sudo postfix stop`

- Очистить почтовую очередь:

`sudo postfix flush`

- Перезагрузить файлы конфигурации:

`sudo postfix reload`
