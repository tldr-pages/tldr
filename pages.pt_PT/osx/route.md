# route

> Alteração manual da tabela de rotas.
> Necessita de root.

- Adicionar uma rota para um destino passando por um gateway:

`sudo route add {{endereco_ip_destino}} {{endereco_gateway}}`

- Adicionar uma rota para um rede /24 passando por um gateway:

`sudo route add {{endereco_ip_subnet}}/24 {{endereco_gateway}}`

- Correr em modo de teste (não realiza alterações, apenas a mostra):

`sudo route -t add {{endereco_ip_destino}}/24 {{endereco_gateway}}`

- Remover todas as rotas:

`sudo route flush`

- Remover uma rota especifica:

`sudo route delete {{endereco_ip_destino}}/24`

- Procurar e mostrar a rota para um destino (nome da máquina ou endereço IP)

`sudo route get {{destino}}`