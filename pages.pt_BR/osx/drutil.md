# drutil

> Interage com gravadores de DVD.
> Mais informações: <https://keith.github.io/xcode-man-pages/drutil.1.html>.

- Ejeta um disco da unidade:

`drutil eject`

- Grava um diretório como um sistema de arquivos ISO9660 em um DVD. Não verifica, e ejeta quando terminar:

`drutil burn -noverify -eject -iso9660`
