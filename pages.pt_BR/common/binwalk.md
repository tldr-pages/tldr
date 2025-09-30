# binwalk

> Ferramenta de análise de Firmware.
> Mais informações: <https://github.com/ReFirmLabs/binwalk>.

- Escaneia um arquivo binário:

`binwalk {{caminho/para/binário}}`

- Extrai arquivos de um binário, especificando a saída do diretório:

`binwalk {{[-e|--extract]}} {{[-C|--directory]}} {{diretório_do_destino}} {{caminho/para/binário}}`

- Extrai recursivamente arquivos de um binário limitando a profundidade da recursão para 2:

`binwalk {{[-e|--extract]}} {{[-M|--matryoshka]}} {{[-d|--depth]}} {{2}} {{caminho/para/binário}}`

- Extrai arquivos de um binário com uma assinatura específica:

`binwalk {{[-D|--dd]}} '{{png image:png}}' {{caminho/para/binário}}`

- Analisa a entropia de um binário, salvando o gráfico com o mesmo nome que o binário e a extensão `.png`:

`binwalk {{[-E|--entropy]}} {{[-J|--save]}} {{caminho/para/binário}}`

- Combina entropia, assinatura e análise dos código de operações em um comando só:

`binwalk {{[-E|--entropy]}} {{[-B|--signature]}} {{[-A|--opcodes]}} {{caminho/para/binário}}`
