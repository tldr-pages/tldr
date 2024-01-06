# fdesetup

> Define e recupera informações relacionadas ao FileVault.
> Mais informações: <https://www.unix.com/man-page/mojave/8/fdesetup/>.

- Lista os usuários atuais habilitados para o FileVault:

`sudo fdesetup list`

- Obtém o status atual do FileVault:

`fdesetup status`

- Adiciona usuário habilitado para o FileVault:

`sudo fdesetup add -usertoadd {{usuário1}}`

- Ativa o FileVault:

`sudo fdesetup enable`

- Desativa o FileVault:

`sudo fdesetup disable`
