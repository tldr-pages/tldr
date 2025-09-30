# dig

> Utilitário de pesquisa de DNS.
> Mais informações: <https://manned.org/dig>.

- Pesquisa o(s) IP(s) associados a um hostname (registros A):

`dig +short {{example.com}}`

- Obtém uma resposta detalhada para um determinado domínio (registros A):

`dig +noall +answer {{example.com}}`

- Consulta um tipo de registro DNS específico associado a um nome de domínio fornecido:

`dig +short {{example.com}} {{A|MX|TXT|CNAME|NS}}`

- Especifica um DNS alternativo para busca e opcionalmente usa DNS sobre TLS (DoT):

`dig {{+tls}} @{{1.1.1.1|8.8.8.8|9.9.9.9|...}} {{example.com}}`

- Performa uma busca reversa de DNS em um endereço de IP (registro PTR):

`dig -x {{8.8.8.8}}`

- Encontra servidores de nomes autorizados para a região e exibe os registros SOA:

`dig +nssearch {{example.com}}`

- Performa consultas iterativas e exibe o caminho de ratreio completo para resolver um nome de domínio:

`dig +trace {{example.com}}`

- Busca um servidor DNS sobre uma [p]orta não padrão usando protocolo TCP:

`dig +tcp -p {{porta}} @{{ip_servidor_dns}} {{example.com}}`
