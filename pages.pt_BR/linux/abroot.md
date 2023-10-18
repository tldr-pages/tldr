# abroot

> O utilitário ABRoot fornece total imutabiliodade e atomicidade ao transacionar entre 2 estados da partição raíz (A⟺B).
> Isso também permite transações sob demanda via um shell transacional.
> Mais informações: <https://github.com/Vanilla-OS/ABRoot>.

- Saída do estado da partição raiz atual ou futuro:

`sudo abroot get {{present|future}}`

- Insira um shell transacional na futura partição raiz e alterne o root na próxima inicialização:

`sudo abroot shell`

- Executa um comando específico no shell transacional na partição raíz futura e troca para ela na próxima inicialização:

`sudo abroot exec "{{comando}}"`

- Instala pacotes específicos no servidor dentro do shell transacional na partição raíz futura e troca para ela na próxima inicialização:

`sudo abroot exec apt install {{pacote1 pacote2 ...}}`

- Atualiza a partição de inicialização (apenas para usuários avançados):

`sudo abroot _update-boot`

- Exibe ajuda:

`abroot --help`

- Exibe versão:

`abroot --version`
