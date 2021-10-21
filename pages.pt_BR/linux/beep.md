# beep

> Utilitário que permite o computador emitir sons.
> Mais informações: <https://github.com/spkr-beep/beep>.

- Emitir um som:

`beep`

- Emitir um som repetidamente:

`beep -r {{repeticoes}}`

- Emitir um som em uma frequência (Hz) específica e com duração específica (milisegundos):

`beep -f {{frequencia}} -l {{duracao}}`

- Emitir cada frequência e duração como um som diferente:

`beep -f {{frequencia}} -l {{duracao}} -n -f {{frequencia}} -l {{duracao}}`

- Executar a escala de Dó maior:

`beep -f {{262}} -n -f {{294}} -n -f {{330}} -n -f {{349}} -n -f {{392}} -n -f {{440}} -n -f {{494}} -n -f {{523}}`
