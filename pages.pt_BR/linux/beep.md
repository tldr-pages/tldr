# beep

> Utilitário que permite o computador emitir sons.
> Mais informações: <https://github.com/spkr-beep/beep>.

- Emite um som:

`beep`

- Emite um som repetidamente:

`beep -r {{repeticoes}}`

- Emite um som em uma frequência (Hz) específica e com duração específica (milisegundos):

`beep -f {{frequencia}} -l {{duracao}}`

- Emite cada frequência e duração como um som diferente:

`beep -f {{frequencia}} -l {{duracao}} -n -f {{frequencia}} -l {{duracao}}`

- Executa a escala de Dó maior:

`beep -f {{262}} -n -f {{294}} -n -f {{330}} -n -f {{349}} -n -f {{392}} -n -f {{440}} -n -f {{494}} -n -f {{523}}`
