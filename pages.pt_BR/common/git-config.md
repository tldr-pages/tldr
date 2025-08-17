# git config

> Gerencia configurações personalizadas para repositórios Git.
> Estas configurações podem ser locais (para o repositório atual) ou globais (para o usuário atual).
> Mais informações: <https://git-scm.com/docs/git-config>.

- Define globalmente seu nome ou e-mail (essas informações são necessárias para fazer commit em um repositório e serão incluídas em todos os commits):

`git config --global {{user.name|user.email}} "{{Seu nome|e-mail@example.com}}"`

- Lista configurações locais ou globais:

`git config {{[-l|--list]}} --{{local|global}}`

- Lista somente configurações do sistema (armazenadas no `/etc/gitconfig`), e exibe o local do arquivo:

`git config {{[-l|--list]}} --system --show-origin`

- Obtém o valor de uma dada configuração:

`git config alias.unstage`

- Define o valor global de uma dada configuração:

`git config --global alias.unstage "reset HEAD --"`

- Reverte a configuração global para seu valor padrão:

`git config --global --unset alias.unstage`

- Edita a configuração local do Git (`.git/config`) no editor padrão:

`git config {{[-e|--edit]}}`

- Edita a configuração global do Git (`~/.gitconfig` por padrão ou `$XDG_CONFIG_HOME/git/config` se tal arquivo existir) no editor padrão:

`git config --global {{[-e|--edit]}}`
