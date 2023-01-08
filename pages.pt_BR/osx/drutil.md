# drutil

> Interage com gravadores de DVD.
> Mais informações: <https://ss64.com/osx/drutil.html>.

- Ejeta um disco da unidade:

`drutil eject`

- Grava um diretório como um sistema de arquivos ISO9660 em um DVD. Não verifica, e ejeta quando terminar:

`drutil burn -noverify -eject -iso9660`
