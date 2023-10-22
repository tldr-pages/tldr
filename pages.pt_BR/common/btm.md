# btm

> Uma alternativa ao `top`.
> Tem como objetivo ser leve, multiplataforma e mais gráfico que o `top`.
> Mais informações: <https://github.com/ClementTsang/bottom>.

- Exibe o layout padrão (CPU, memória, temperaturas, disco, rede e processos):

`btm`

- Ativa o modo básico, removendo gráficos e condensando dados (semelhante a `top`):

`btm --basic`

- Usa pontos grandes em vez de pequenos em gráficos:

`btm --dot_marker`

- Exibe também a carga da bateria e o estado de saúde:

`btm --battery`

- Atualiza a cada 250 milissegundos e exibe os últimos 30 segundos nos gráficos:

`btm --rate 250 --default_time_value 30000`
