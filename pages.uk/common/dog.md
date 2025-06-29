# dog

> Утиліта пошуку DNS.
> Вона має кольоровий вихід, підтримує протоколи DNS-over-TLS і DNS-over-HTTPS та може видавати JSON.
> Більше інформації: <https://github.com/ogham/dog#examples>.

- Шукає IP-адреси пов'язані з іменем хоста (A records):

`dog {{example.com}}`

- Запитує тип записів MX, пов’язаних із заданим доменним ім’ям:

`dog {{example.com}} MX`

- Вкажіть конкретний DNS-сервер для запиту (наприклад, Cloudflare):

`dog {{example.com}} MX @{{1.1.1.1}}`

- Запит через TCP, а не UDP:

`dog {{example.com}} MX @{{1.1.1.1}} {{[-T|--tcp]}}`

- Запитує тип записів MX, пов’язаних із заданим доменним ім’ям через TCP, використовуючи явні аргументи:

`dog {{[-q|--query]}} {{example.com}} {{[-t|--type]}} MX {{[-n|--nameserver]}} {{1.1.1.1}} {{[-T|--tcp]}}`

- Шукає IP-адреси, пов’язані з іменем хоста (записи A), за допомогою DNS через HTTPS (DoH):

`dog {{example.com}} {{[-H|--https]}} @{{https://cloudflare-dns.com/dns-query}}`
