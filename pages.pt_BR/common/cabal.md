# cabal

> Interface de linha de comando para a infraestrutura de pacote Haskel (Cabal).
> Gerencia projetos Haskell e pacotes Cabal do repositório de pacotes Hackage.
> Mais informações: <https://cabal.readthedocs.io/en/latest/intro.html>.

- Busca e lista pacotes do Hackage:

`cabal list {{string_buscada}}`

- Mostra informações sobre o pacote:

`cabal info {{nome_pacote}}`

- Baixa e instala um pacote:

`cabal install {{nome_pacote}}`

- Cria um novo projeto Haskell no diretório atual:

`cabal init`

- Monta o projeto no diretório atual:

`cabal build`

- Roda testes do projeto no diretório atual:

`cabal test`
