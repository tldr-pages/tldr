# beep

> Utilitário para o computador emitir beep.

- Emite um beep:

`beep`

- Emite um beep repetidamente:

`beep -r {{repetitions}}`

- Emite um beep em uma frequência (Hz) específica e com duração específica (milliseconds):

`beep -f {{frequency}} -l {{duration}}`

- Emite cada frequência e duração como um beep diferente:

`beep -f {{frequency}} -l {{duration}} -n -f {{frequency}} -l {{duration}}`

- Executa a escala de Dó maior:

`beep -f 262 -n -f 294 -n -f 330 -n -f 349 -n -f 392 -n -f 440 -n -f 494 -n -f 523`
