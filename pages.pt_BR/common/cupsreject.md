# cupsreject

> Rejeita trabalhos enviados para uma ou mais impressoras.
> NOTA: destino se refere a uma impressora ou uma classe de impressoras.
> Veja também: `cupsaccept`, `cupsenable`, `cupsdisable`, `lpstat`.
> Mais informações: <https://www.cups.org/doc/man-cupsaccept.html>.

- Rejeita trabalhos para os destinos especificados:

`cupsreject {{destino1 destino2 ...}}`

- Especifica um servidor diferente:

`cupsreject -h {{servidor}} {{destino1 destino2 ...}}`

- Especifica uma mensagem de motivo ("Reason Unknown" por padrão):

`cupsreject -r {{motivo}} {{destino1 destino2 ...}}`
