# ab

> Ferramenta da Apache para realizar benchmarking e testes de carga em servidores web.
> Mais informações: <https://httpd.apache.org/docs/2.4/programs/ab.html>.

- Executar 100 requisições HTTP do tipo GET para uma determinada URL:

`ab -n {{100}} {{url}}`

- Executar 100 requisições HTTP do tipo GET para uma determinada URL, executando 10 requisições simultâneas de cada vez:

`ab -n {{100}} -c {{10}} {{url}}`

- Utilizar a funcionalidade HTTP Keep Alive, permitindo que várias requisições sejam feitas em uma sessão HTTP:

`ab -k {{url}}`

- Definir o tempo total do benchmarking, em segundos:

`ab -t {{60}} {{url}}`
