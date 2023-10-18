# zsh

> Z SHell, um interpretador de linha de comando compatível com o Bash.
> Veja também `bash`, `histexpand`.
> Mais informações: <https://www.zsh.org>.

- Inicie uma sessão shell interativa:

`zsh`

- Execute [c]omandos específicos:

`zsh -c "{{echo Olá Mundo}}"`

- Execute um script específico:

`zsh {{caminho/para/script.zsh}}`

- Verifica um script específico por erros de sintaxe sem executá-lo:

`zsh --no-exec {{caminho/para/script.zsh}}`

- Executa comandos específicos da `stdin`:

`{{echo Olá Mundo}} | zsh`

- Execute um script específico, imprimindo cada comando do script antes de executá-lo:

`zsh --xtrace {{caminho/para/script.zsh}}`

- Inicie uma sessão shell interativa no modo verboso, imprimindo cada comando antes de executá-lo:

`zsh --verbose`

- Executa um comando específico dentro do `zsh` com padrões glob desativados:

`noglob {{comando}}`
