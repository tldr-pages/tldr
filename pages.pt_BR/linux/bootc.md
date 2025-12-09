# bootc

> Inicializa e atualiza seu sistema usando imagens de containeres.
> Manipula atualizações transacionais e transparentes utilizando imagens de containeres OCI/Docker.
> Mais informações: <https://manned.org/bootc.8>.

- Mostra todos os deployments na ordem que eles aparecem na inicialização:

`bootc status`

- Mostra se há alguma atualização disponível:

`bootc upgrade --check`

- Atualiza e reinicia o sistema:

`bootc upgrade --apply`

- Move seu sistema para outra base:

`bootc switch {{imagem}}`

- Reinicia o seu sistema no deployment anterior:

`bootc rollback`
