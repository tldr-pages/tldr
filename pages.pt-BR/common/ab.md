# ab

> Ferramenta de benchmarking do servidor Apache. A ferramenta mais simples para realizar testes de carga.
> Página oficial: <https://httpd.apache.org/docs/2.4/programs/ab.html>.

- Executar 100 requisições HTTP do tipo GET para uma determinada URL:

`ab -n {{100}} {{url}}`

- Executar 100 requisições HTTP do tipo GET para uma determinada URL. Sendo que as requisições concorrentes acontecerão em grupos de 10:

`ab -n {{100}} -c {{10}} {{url}}`

- Utilizar a funcionalidade HTTP _Keep Alive_, permitindo que várias requisições sejam feitas em uma sessão HTTP:

`ab -k {{url}}`

- Definir o tempo total do _benchmarking_, em segundos:

`ab -t {{60}} {{url}}`
