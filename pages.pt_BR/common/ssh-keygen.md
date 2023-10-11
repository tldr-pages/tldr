# ssh-keygen

> Gera chaves SSH usadas para autenticação, logins sem senha e outras finalidades.
> Mais informações: <https://man.openbsd.org/ssh-keygen>.

- Gerar uma chave interativamente:

`ssh-keygen`

- Gerar uma chave ed25519 com 32 rounds de função de derivação de chave e salvar a chave em um arquivo específico:

`ssh-keygen -t {{ed25519}} -a {{32}} -f {{~/.ssh/nome_do_arquivo}}`

- Gerar uma chave RSA de 4096 bits com um comentário de email:

`ssh-keygen -t {{rsa}} -b {{4096}} -C "{{comentário|email}}"`

- Remover as chaves de um host do arquivo known_hosts (útil quando um host conhecido tem uma nova chave):

`ssh-keygen -R {{host_remoto}}`

- Obter a impressão digital de uma chave em MD5 Hex:

`ssh-keygen -l -E {{md5}} -f {{~/.ssh/nome_do_arquivo}}`

- Alterar a senha de uma chave:

`ssh-keygen -p -f {{~/.ssh/nome_do_arquivo}}`

- Alterar o tipo de formato da chave (por exemplo, de formato OPENSSH para PEM), o arquivo será reescrito no local:

`ssh-keygen -p -N "" -m {{PEM}} -f {{~/.ssh/chave_privada_OpenSSH}}`

- Obter a chave pública a partir da chave secreta:

`ssh-keygen -y -f {{~/.ssh/chave_privada_OpenSSH}}`
