# abroot

> Utilitário que fornece total imutabilidade e atomicidade ao transacionar entre 2 estados da partição raíz (A⟺B).
> Atualizações são realizadas usando imagens OCI, para garantir que o sistema sempre estará em um estado consistente.
> Mais informações: <https://docs.vanillaos.org/docs/en/abroot-manpage>.

- Adiciona pacotes à imagem local (Nota: após executar esse comando você precisa aplicar as alterações.):

`sudo abroot pkg add {{pacote}}`

- Remove pacotes da imagem local(Nota: após executar esse comando você precisa aplicar as alterações.):

`sudo abroot pkg remove {{pacote}}`

- Lista pacotes da imagem local:

`sudo abroot pkg list`

- Aplica mudanças à imagem local (Nota: você precisa reiniciar o sistema para que as mudanças sejam aplicadas):

`sudo abroot pkg apply`

- Reverte o sistema para o estado anterior:

`sudo abroot rollback`

- Edita/Mostra os parâmetros do kernel:

`sudo abroot kargs {{edit|show}}`

- Mostra o estado:

`sudo abroot status`

- Exibe ajuda:

`abroot {{[-h|--help]}}`
