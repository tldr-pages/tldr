# btm

> Uma alternativa ao `top`.
> Tem como objetivo ser leve, multiplataforma e mais gráfico que o `top`.
> Veja também: `btop`, `glances`, `atop`, `htop`, `top`, `sensors`.
> Mais informações: <https://clementtsang.github.io/bottom/nightly/#usage-and-configuration>.

- Exibe o layout padrão (CPU, memória, temperaturas, disco, rede e processos):

`btm`

- Ativa o modo básico, removendo gráficos e condensando dados (semelhante a `top`):

`btm {{[-b|--basic]}}`

- Usa pontos grandes em vez de pequenos em gráficos:

`btm {{[-m|--dot_marker]}}`

- Exibe também a carga da bateria e o estado de saúde:

`btm --battery`

- Atualiza a cada 250 milissegundos e exibe os últimos 30 segundos nos gráficos:

`btm {{[-r|--rate]}} 250 {{[-t|--default_time_value]}} 30000`
