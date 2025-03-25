# asdf

> Utilitário para a gestão de versões de linguagens e programas.
> Mais informações: <https://asdf-vm.com/manage/commands.html>.

- Lista todos os plugins disponíveis:

`asdf plugin list all`

- Instala um plugin:

`asdf plugin add {{nome}}`

- Lista todas as versões disponíveis para um pacote:

`asdf list all {{nome}}`

- Instala uma versão específica de um pacote:

`asdf install {{nome}} {{versão}}`

- Define a versão global de um pacote:

`asdf set -u {{nome}} {{versão}}`

- Define a versão local de um pacote:

`asdf set {{nome}} {{versão}}`

- Ver a versão utilizada para um pacote:

`asdf current {{name}}`
