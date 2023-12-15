# lpadmin

> Configura impressoras e classes do CUPS.
> Veja também: `lpoptions`.
> Mais informações: <https://www.cups.org/doc/man-lpadmin.html>.

- Definir a impressora padrão:

`lpadmin -d {{impressora}}`

- Excluir uma impressora ou classe específica:

`lpadmin -x {{impressora|classe}}`

- Adicionar uma impressora a uma classe:

`lpadmin -p {{impressora}} -c {{classe}}`

- Remover uma impressora de uma classe:

`lpadmin -p {{impressora}} -r {{classe}}`
