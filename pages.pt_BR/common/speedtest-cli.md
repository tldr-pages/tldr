# speedtest-cli

> Teste a largura de banda da Internet usando <https://speedtest.net>.
> Veja também: `speedtest` para a aplicação CLI oficial.
> Mais informações: <https://github.com/sivel/speedtest-cli>.

- Executa um teste de velocidade:

`speedtest-cli`

- Executa um teste de velocidade e exibe valores em bytes, ao invés de bits:

`speedtest-cli --bytes`

- Executa um teste de velocidade usando `HTTPS`, ao invés de `HTTP`:

`speedtest-cli --secure`

- Executa um teste de velocidade sem realizar testes de download:

`speedtest-cli --no-download`

- Executa um teste de velocidade e gera uma imagem dos resultados:

`speedtest-cli --share`

- Lista todos os servidores `speedtest.net`, classificados por distância:

`speedtest-cli --list`

- Executa um teste de velocidade a um servidor do speedtest.net específico:

`speedtest-cli --server {{id_do_servidor}}`

- Executa um teste de velocidade e exibe os resultados como JSON (suprime informações de progresso):

`speedtest-cli --json`
