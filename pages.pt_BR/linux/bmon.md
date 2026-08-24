# bmon

> Monitora a largura de banda e produz estatísticas relacionadas a rede.
> Mais informações: <https://manned.org/bmon>.

- Exibe uma lista com todas as interfaces de rede:

`bmon {{[-a|--show-all]}}`

- Exibe as taxas de transferência de dados em bits por segundo:

`bmon {{[-b|--use-bit]}}`

- Define quais interfaces serão visíveis:

`bmon {{[-p|--policy]}} {{interface_1,interface_2,interface_3}}`

- Define o intervalo (em segundos) que a taxa por contador será calculada:

`bmon {{[-R|--rate-interval]}} {{2.0}}`
