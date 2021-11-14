# systemsetup

> Configura as definições de Preferencias do Sistema da máquina
> Mais informações: <https://ss64.com/osx/systemsetup.html>.

- Ativa autenticação remota (SSH):

`systemsetup -setremotelogin on`

- Ativa o serviço de hora de rede com um fuso horário e servidor específico:

`systemsetup -settimezone {{Europe/Lisbon}} -setnetworktimeserver {{2.pt.pool.ntp.org}} -setusingnetworktime on`

- Colaca a máquina sem dormir, reiniciando automaticamente em falta de energia ou pânico do núcleo do sistema:

`systemsetup -setsleep off -setrestartpowerfailure on -setrestartfreeze on`

- Lista os discos de inicialização validos:

`systemsetup -liststartupdisks`

- Especifica um novo disco de inicialização:

`systemsetup -setstartupdisk {{caminho}}`
