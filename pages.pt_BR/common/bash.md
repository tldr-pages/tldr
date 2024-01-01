# bash

> Bourne-Again SHell, um interpretador de linha de comando compatível com `sh`.
> Veja também: `zsh`, `histexpand` (expansão do histórico).
> Mais informações: <https://www.gnu.org/software/bash/>.

- Inicia uma sessão interativa do shell:

`bash`

- Inicia uma sessão interativa do shell sem carregar as configurações de inicialização:

`bash --norc`

- Executa [c]omandos específicos:

`bash -c "{{echo 'bash é executado'}}"`

- Executa um script específico:

`bash {{caminho/para/script.sh}}`

- Executa um script específico exibindo cada comando antes de executá-lo:

`bash -x {{caminho/para/script.sh}}`

- Executa um script específico e para no primeiro [e]rro:

`bash -e {{caminho/para/script.sh}}`

- Executa comandos específicos da `stdin`:

`{{echo "echo 'bash é executado'"}} | bash`

- Inicia uma sessão do shell [r]estrita:

`bash -r`
