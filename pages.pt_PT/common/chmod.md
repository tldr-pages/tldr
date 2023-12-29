# chmod

> Alterar as permissões de acesso a um ficheiro ou diretório.
> Mais informações: <https://www.gnu.org/software/coreutils/chmod>.

- Dá a um [u]tilizador que possui um ficheiro o direito a e[x]ecutá-lo:

`chmod u+x {{caminho/para/ficheiro}}`

- Dá a um [u]tilizador direitos para le[r] e escreve ([w]) num ficheiro/diretório:

`chmod u+rw {{caminho/para/ficheiro_ou_diretório}}`

- Remove direitos de execução de um [g]rupo:

`chmod g-x {{caminho/para/ficheiro}}`

- Dá a todos ([a]) os utilizadores o direito de le[r] e e[x]ecutar:

`chmod a+rx {{caminho/para/ficheiro}}`

- Dá a [o]utros (que não estão no grupo do dono do ficheiro) os mesmos direitos do [g]rupo:

`chmod o=g {{caminho/para/ficheiro}}`

- Remove todos os direitos dos [o]utros:

`chmod o= {{caminho/para/ficheiro}}`

- Muda as permissões, recursivamente, dando ao [g]rupo e [o]utros a possibilidade de escrever ([w]):

`chmod -R g+w,o+w {{caminho/para/diretório}}`
