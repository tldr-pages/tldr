# lpadmin

> Configura impressoras e classes do CUPS.
> Veja também: `lpoptions`.
> Mais informações: <https://www.cups.org/doc/man-lpadmin.html>.

- Define a impressora padrão:

`lpadmin -d {{impressora}}`

- Exclui uma impressora ou classe específica:

`lpadmin -x {{impressora|classe}}`

- Adiciona uma impressora a uma classe:

`lpadmin -p {{impressora}} -c {{classe}}`

- Remove uma impressora de uma classe:

`lpadmin -p {{impressora}} -r {{classe}}`
