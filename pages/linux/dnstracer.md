# dnstracer

> The dnstracer command determines where a DNS gets its information from.
> More information: <https://manned.org/dnstracer>.

- Find out where your local DNS got the information on www.example.com:

`dnstracer {{www.example.com}}`

- Start with a [s]pecific DNS that you already know:

`dnstracer -s {{dns.example.org}} {{www.example.com}}`

- Only query IPv4 servers:

`dnstracer -4 {{www.example.com}}`

- Retry each request 5 times on failure:

`dnstracer -r {{5}} {{www.example.com}}`

- Display all steps during execution:

`dnstracer -v {{www.example.com}}`

- Display an [o]verview of all received answers after execution:

`dnstracer -o {{www.example.com}}`
