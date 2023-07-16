# sshd

> Daemon do Secure Shell - permite que máquinas remotas façam login de forma segura na máquina atual.
> Máquinas remotas podem executar comandos como se estivessem sendo executados nesta máquina.
> Mais informações: <https://man.openbsd.org/sshd>.

- Iniciar o daemon em segundo plano:

`sshd`

- Executar o sshd em primeiro plano:

`sshd -D`

- Executar com saída detalhada (para depuração):

`sshd -D -d`

- Executar em uma porta específica:

`sshd -p {{porta}}`
