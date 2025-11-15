# dnf

> Gerenciador de pacotes das distribuições baseadas em RHEL (substituto do yum).
> Para comandos equivalentes em outros gerenciadores de pacotes, veja <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Mais informações: <https://dnf.readthedocs.io>.

- Atualiza os pacotes instalados para suas versões mais atuais:

`sudo dnf upgrade`

- Busca pacotes com palavras-chave:

`dnf search {{palavra_chave1 palavra_chave2 ...}}`

- Mostra detalhes sobre um determinado pacote:

`dnf info {{pacote}}`

- Instala um novo pacote (use `-y` para responder sim à todos os prompts):

`sudo dnf install {{pacote1 pacote2 ...}}`

- Remove um pacote:

`sudo dnf remove {{pacote1 pacote2 ...}}`

- Lista pacotes intalados:

`dnf list --installed`

- Busca por pacotes que fornecem um dado comando:

`dnf provides {{comando}}`

- Mostra todas as operações passadas:

`dnf history`
