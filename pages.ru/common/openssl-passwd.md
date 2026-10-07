# openssl passwd

> Генерировать хеш пароля.
> Больше информации: <https://docs.openssl.org/master/man1/openssl-passwd/>.

- Сгенерировать хеш пароля по алгоритму SHA256 (только Linux):

`openssl passwd -5`

- Сгенерировать хеш пароля по алгоритму APR1:

`openssl passwd -apr1`

- Сгенерировать хеш пароля по алгоритму APR1 с солью:

`openssl passwd -apr1 -salt {{строка_соли}}`

- Сгенерировать хеш пароля по алгоритму APR1 и отобразить пароль вместе с хешем:

`openssl passwd -apr1 -table`

- Сгенерировать хеш пароля из `stdin`:

`echo -n "{{пароль}}" | openssl passwd {{-apr1}} -stdin`
