# chmod

> Muda a permissão de acesso de um arquivo ou diretório.
> Mais informações: <https://www.gnu.org/software/coreutils/chmod>.

- Dá ao [u]suário dono de um arquivo o direito de e[x]ecutá-lo:

`chmod u+x {{arquivo}}`

- Dá ao [u]suário direitos para le[r] e [w]escrever em um arquivo/diretório:

`chmod u+rw {{arquivo_ou_diretorio}}`

- Remove direitos e[x]ecutáveis de um [g]rupo:

`chmod g-x {{arquivo}}`

- Dá a [a]todos os usuários direitos para le[r] e e[x]ecutar:

`chmod a+rx {{arquivo}}`

- Dá para [o]utros (que não estejam no grupo do proprietário do arquivo) os mesmos direitos que o [g]rupo:

`chmod o=g {{arquivo}}`

- Remove todos os direitos de [o]utros:

`chmod o= {{arquivo}}`

- Muda recursivamente as permissões, dando para [g]rupo e [o]utros a habilidade para [w]escrever:

`chmod -R g+w,o+w {{diretorio}}`

- Recursivamente concede a [a]todos os usuários permissões de leitu[r]a para arquivos e e[X]ecute permissões para sub-diretórios dentro de um diretório:

`chmod -R a+rX {{diretorio}}`
