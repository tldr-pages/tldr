# dpkg-buildpackage

> Compila pacotes binários e/ou fonte no formato Debian a partir do código-fonte.
> Normalmente é executado dentro de uma árvore de fontes que contém um diretório `debian/`.
> Também pode verificar dependências de compilação, gerar arquivos como `.buildinfo` e `.changes`, e assinar o resultado quando aplicável.
> Mais informações: <https://manned.org/dpkg-buildpackage>.

- Gera pacotes fonte e binário:

`dpkg-buildpackage`

- Gera apenas pacotes binários (sem pacote fonte):

`dpkg-buildpackage {{[-b|--build=binary]}}`

- Gera apenas o pacote fonte (sem compilar binários):

`dpkg-buildpackage {{[-S|--build=source]}}`

- Não assina os arquivos `.dsc` e `.changes`:

`dpkg-buildpackage {{[-us|--unsigned-source]}} {{[-uc|--unsigned-changes]}}`

- Não executa `clean` antes de compilar:

`dpkg-buildpackage {{[-nc|--no-pre-clean]}}`

- Usa `fakeroot` como comando para obter privilégios de root durante o build:

`dpkg-buildpackage {{[-r|--root-command=]}}{{fakeroot}}`

- Executa um alvo específico de `debian/rules`:

`dpkg-buildpackage {{[-T|--rules-target=]}}{{clean}}`
