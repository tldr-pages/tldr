# pactl

> Controla um servidor PulseAudio em execução.
> Mais informações: <https://manned.org/pactl>.

- Mostra informações sobre o servidor de áudio:

`pactl info`

- Lista todas as sinks (ou outros tipos - sinks são saídas e sink-inputs são fluxos de áudio ativos):

`pactl list {{sinks}} short`

- Altera a sink padrão (saída) para 1 (o número pode ser obtido através do subcomando `list`):

`pactl set-default-sink {{1}}`

- Move a sink-input 627 para a sink 1:

`pactl move-sink-input {{627}} {{1}}`

- Define o volume da sink 1 para 75%:

`pactl set-sink-volume {{1}} {{0.75}}`

- Ativa/Desativa o modo silencioso na sink padrão (usando o nome especial `@DEFAULT_SINK@`):

`pactl set-sink-mute {{@DEFAULT_SINK@}} toggle`
