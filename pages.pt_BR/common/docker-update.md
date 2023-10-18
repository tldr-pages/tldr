# docker update

> Atualizar a configuração de contêineres Docker.
> Este comando não é suportado para contêineres Windows.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/update/>.

- Atualizar a política de reinicialização a ser aplicada quando um contêiner específico for encerrado:

`docker update --restart={{always|no|on-failure|unless-stopped}} {{nome_do_contêiner}}`

- Atualizar a política para reiniciar até três vezes um contêiner específico quando ele for encerrado com status de saída diferente de zero:

`docker update --restart=on-failure:3 {{nome_do_contêiner}}`

- Atualizar o número de CPUs disponíveis para um contêiner específico:

`docker update --cpus {{quantidade}} {{nome_do_contêiner}}`

- Atualizar o limite de memória em [M]egabytes para um contêiner específico:

`docker update --memory {{limite}}M {{nome_do_contêiner}}`

- Atualizar o número máximo de IDs de processos permitidos dentro de um contêiner específico (use `-1` para ilimitado):

`docker update --pids-limit {{quantidade}} {{nome_do_contêiner}}`

- Atualizar a quantidade de memória em [M]egabytes que um contêiner específico pode trocar para o disco (use `-1` para ilimitado):

`docker update --memory-swap {{limite}}M {{nome_do_contêiner}}`
