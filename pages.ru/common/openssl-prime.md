# openssl prime

> Вычислять простые числа.
> Больше информации: <https://docs.openssl.org/master/man1/openssl-prime/>.

- Сгенерировать простое число длиной 2048 бит и отобразить его в шестнадцатеричном формате:

`openssl prime -generate -bits 2048 -hex`

- Проверить, является ли указанное число простым:

`openssl prime {{число}}`
