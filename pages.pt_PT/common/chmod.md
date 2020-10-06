# chmod

> Alterar as permissões de acesso a um ficheiro ou diretório.

- Dar a um [u]tilizador que possui um ficheiro o direito a e[x]ecutá-lo:

`chmod u+x {{ficheiro}}`

- Dar a um [u]tilizador direitos para le[r] e escrever ([w]) num ficheiro/diretório:

`chmod u+rw {{ficheiro_ou_diretorio}}`

- Remover direitos de execução de um [g]rupo:

`chmod g-x {{ficheiro}}`

- Dar a todos ([a]) os utilizadores o direito de le[r] e e[x]ecutar:

`chmod a+rx {{ficheiro}}`

- Dar a [o]utros (que não estão no grupo do dono do ficheiro) os mesmos direitos do [g]rupo:

`chmod o=g {{ficheiro}}`

- Remover todos os direitos dos [o]utros:

`chmod o= {{ficheiro}}`

- Mudar as permissões, recursivamente, dando ao [g]rupo e [o]utros a possibilidade de escrever ([w]):

`chmod -R g+w,o+w {{diretorio}}`
