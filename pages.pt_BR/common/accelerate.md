# accelerate

> Uma biblioteca que habilita o mesmo código PyTorch a rodar em qualquer configuração distribuída.
> Mais informações: <https://huggingface.co/docs/accelerate/index>.

- Mostra informações do ambiente:

`accelerate env`

- Cria um arquivo de configuração de forma interativa:

`accelerate config`

- Mostra o custo de memória de GPU estimado para rodar um Modelo de Face aumentado com diferentes tipos de dados:

`accelerate estimate-memory {{nome/modelo}}`

- Testa um arquivo Accelerate de configuração:

`accelerate test --config_file {{caminho/para/config.yaml}}`

- Roda um modelo na CPU com Accelerate:

`accelerate launch {{caminho/para/script.py}} {{--cpu}}`

- Roda um modelo em multi-GPU com Accelerate, com 2 máquinas:

`accelerate launch {{caminho/para/script.py}} --multi_gpu --num_machines 2`
