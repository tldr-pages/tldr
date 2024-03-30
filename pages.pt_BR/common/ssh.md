# ssh

> O Secure Shell é um protocolo usado para fazer login de forma segura em sistemas remotos.
> Ele pode ser usado para fazer login ou executar comandos em um servidor remoto.
> Mais informações: <https://man.openbsd.org/ssh>.

- Conecta a um servidor remoto:

`ssh {{nome_do_usuário}}@{{host_remoto}}`

- Conecta a um servidor remoto com uma identidade específica (chave privada):

`ssh -i {{caminho/para/arquivo_de_chave}} {{nome_do_usuário}}@{{host_remoto}}`

- Conecta a um servidor remoto usando uma porta específica:

`ssh {{nome_do_usuário}}@{{host_remoto}} -p {{2222}}`

- Executa um comando em um servidor remoto com uma alocação de [t]ty permitindo interação com o comando remoto:

`ssh {{nome_do_usuário}}@{{host_remoto}} -t {{comando}} {{argumentos_do_comando}}`

- Tunelamento SSH: Encaminhamento dinâmico de porta (proxy SOCKS em `localhost:1080`):

`ssh -D {{1080}} {{nome_do_usuário}}@{{host_remoto}}`

- Tunelamento SSH: Encaminha uma porta específica (`localhost:9999` para `example.org:80`), desativa a alocação de pseudo-[t]ty e execução de comandos remotos:

`ssh -L {{9999}}:{{example.org}}:{{80}} -N -T {{nome_do_usuário}}@{{host_remoto}}`

- Salta com SSH: Conecta a um servidor remoto através de um host intermediário (vários saltos intermediários podem ser especificados separados por vírgula):

`ssh -J {{nome_do_usuário}}@{{host_intermediário}} {{nome_do_usuário}}@{{host_remoto}}`

- Encaminhamento do agente: Encaminhar as informações de autenticação para a máquina remota (consulte `man ssh_config` para opções disponíveis):

`ssh -A {{nome_do_usuário}}@{{host_remoto}}`
