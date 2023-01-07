# binwalk

> Ferramenta de análise de Firmware.
> Mais informações: <https://github.com/ReFirmLabs/binwalk>.

- Escaneia um arquivo binário:

`binwalk {{caminho/para/binário}}`

- Extrai arquivos de um binário, especificando a saída do diretório:

`binwalk --extract --directory {{diretório_do_destino}} {{caminho/para/binário}}`

- Extrai recursivamente arquivos de um binário limitando a profundidade da recursão para 2:

`binwalk --extract --matryoshka --depth {{2}} {{caminho/para/binário}}`

- Extrai arquivos de um binário com uma assinatura específica:

`binwalk --dd '{{png image:png}}' {{caminho/para/binário}}`

- Analisa a entropia de um binário, salvando o gráfico com o mesmo nome que o binário e a extensão `.png`:

`binwalk --entropy --save {{caminho/para/binário}}`

- Combina entropia, assinatura e análise dos código de operações em um comando só:

`binwalk --entropy --signature --opcodes {{caminho/para/binário}}`
