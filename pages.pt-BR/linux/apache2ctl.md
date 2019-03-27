# apache2ctl

> Interface de controle do servidor web HTTP Apache.
> Este comando está disponível nas distribuições baseadas em Debian, para as baseadas em RHEL veja `httpd`.

- Inicia o Apache. Exibe uma mensagem, caso ele já esteja sendo executado:

`sudo apache2ctl start`

- Encerra o Apache:

`sudo apache2ctl stop`

- Reinicia o Apache:

`sudo apache2ctl restart`

- Verifica se o arquivo de configuração está correto sintaticamente:

`sudo apache2ctl -t`

- Lista os módulos carregados:

`sudo apache2ctl -M`
