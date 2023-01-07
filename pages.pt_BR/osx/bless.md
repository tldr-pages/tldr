# bless

> Define a capacidade de inicialização por volume e as opções de disco de inicialização. Set volume boot capability and startup disk options.
> Mais informações: <https://ss64.com/osx/bless.html>.

- Definir um volume somente com Mac OS X ou Darwin, e criar os arquivos BootX e `boot.efi` se necessário:

`bless --folder {{/Volumes/Mac OS X/System/Library/CoreServices}} --bootinfo --bootefi`

- Definir um volume contendo Mac OS 9 ou Mac OS X como o volume ativo:

`bless --mount {{/Volumes/Mac OS}} --setBoot`

- Definir o sistema para NetBoot e transmitir para um servidor disponível:

`bless --netboot --server {{bsdp://255.255.255.255}}`

- Coletar informações sobre o volume atualmente selecionado (conforme determinado pelo firmware), adequado para piping para um programa capaz de analisar listas de propriedades:

`bless --info --plist`
