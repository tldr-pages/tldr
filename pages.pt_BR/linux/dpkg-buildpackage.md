# dpkg-buildpackage

> Compila pacotes binários e/ou fonte no formato Debian a partir do código-fonte.
> Normalmente é executado dentro de uma árvore de fontes que contém um diretório `debian/`.
> Também pode verificar dependências de compilação, gerar arquivos como `.buildinfo` e `.changes`, e assinar o resultado quando aplicável.
> Mais informações: <https://man7.org/linux/man-pages/man1/dpkg-buildpackage.1.html>.

- Gerar pacotes fonte e binário:

`dpkg-buildpackage`

- Gerar apenas pacotes binários (sem pacote fonte):

`dpkg-buildpackage {{[-b|--build=binary]}}`

- Gerar apenas o pacote fonte (sem compilar binários):

`dpkg-buildpackage {{[-S|--build=source]}}`

- Não assinar os arquivos `.dsc` e `.changes`:

`dpkg-buildpackage {{[-us|--unsigned-source]}} {{[-uc|--unsigned-changes]}}`

- Não executar `clean` antes de compilar:

`dpkg-buildpackage {{[-nc|--no-pre-clean]}}`

- Usar `fakeroot` como comando para obter privilégios de root durante o build:

`dpkg-buildpackage {{[-r|--root-command=]}}{{fakeroot}}`

- Executar um alvo específico de `debian/rules`:

`dpkg-buildpackage {{[-T|--rules-target=]}}{{clean}}`

- Compilar em paralelo:

`DEB_BUILD_OPTIONS=parallel={{N}} dpkg-buildpackage`
