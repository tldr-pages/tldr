# sshd

> Daemon do Secure Shell - permite que máquinas remotas façam login de forma segura na máquina atual.
> Máquinas remotas podem executar comandos como se estivessem sendo executados nesta máquina.
> Mais informações: <https://man.openbsd.org/sshd>.

- Inicia o daemon em segundo plano:

`sshd`

- Executa o sshd em primeiro plano:

`sshd -D`

- Executa com saída detalhada (para depuração):

`sshd -D -d`

- Executa em uma porta específica:

`sshd -p {{porta}}`
