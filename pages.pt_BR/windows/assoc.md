# assoc

> Exibir ou alterar associações entre extensões de arquivo e tipos de arquivos.
> Mais informações: <https://learn.microsoft.com/windows-server/administration/windows-commands/assoc>.

- Listar todas as associações entre extensões de arquivo e tipos de arquivos:

`assoc`

- Exibir o tipo de arquivo associado para uma extensão específica:

`assoc {{.txt}}`

- Definir o tipo de arquivo associado para uma extensão específica:

`assoc .{{txt}}={{arquivotxt}}`
