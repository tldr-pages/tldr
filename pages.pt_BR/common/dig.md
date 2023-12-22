# dig

> Utilitário de pesquisa de DNS.
> Mais informações: <https://manned.org/dig>.

- Pesquisa o(s) IP(s) associados a um hostname (Registros A):

`dig +short {{exemplo.com}}`

- Obtém uma resposta detalhada para um determinado domínio (Registros A):

`dig +noall +answer {{exemplo.com}}`

- Consulta um tipo de registro DNS específico associado a um nome de domínio fornecido:

`dig +short {{exemplo.com}} {{A|MX|TXT|CNAME|NS}}`

- Especifica um servidor DNS alternativo para consultar:

`dig @{{8.8.8.8}} {{exemplo.com}}`

- Performa uma busca reversa de DNS em um endereço de IP (Registro PTR):

`dig -x {{8.8.8.8}}`

- Encontra servidores de nomes autorizados para a região e exibe os registros SOA:

`dig +nssearch {{exemplo.com}}`

- Performa consultas iterativas e exibe o caminho de ratreio completo para resolver um nome de domínio:

`dig +trace {{exemplo.com}}`
