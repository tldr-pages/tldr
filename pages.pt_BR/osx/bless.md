# bless

> Define a capacidade de inicialização por volume e as opções de disco de inicialização. Set volume boot capability and startup disk options.
> Mais informações: <https://keith.github.io/xcode-man-pages/bless.1.html>.

- Define um volume somente com Mac OS X ou Darwin e cria os arquivos BootX e `boot.efi` se necessário:

`bless --folder {{/Volumes/Mac OS X/System/Library/CoreServices}} --bootinfo --bootefi`

- Define um volume contendo Mac OS 9 ou Mac OS X como o volume ativo:

`bless --mount {{/Volumes/Mac OS}} --setBoot`

- Define o sistema para NetBoot e transmite para um servidor disponível:

`bless --netboot --server {{bsdp://255.255.255.255}}`

- Coleta informações sobre o volume atualmente selecionado (conforme determinado pelo firmware), adequado para piping para um programa capaz de analisar listas de propriedades:

`bless --info --plist`
