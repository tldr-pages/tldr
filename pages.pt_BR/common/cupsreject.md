# cupsreject

> Rejeita trabalhos enviados para uma ou mais impressoras.
> Veja também: `cupsaccept`.
> Mais informações: <https://www.cups.org/doc/man-cupsaccept.html>.

- Rejeita trabalhos para os destinos especificados:

`cupsreject {{destino1 destino2 ...}}`

- Especificar um servidor diferente:

`cupsreject -h {{servidor}} {{destino1 destino2 ...}}`

- Especificar uma mensagem de motivo ("Reason Unknown" por padrão):

`cupsreject -r {{motivo}} {{destino1 destino2 ...}}`
