# lynis

> Ferramenta de auditoria de sistema e segurança.
> Mais informações: <https://cisofy.com/documentation/lynis/>.

- Verifica se o Lynis está atualizado:

`sudo lynis update info`

- Executa uma auditoria de segurança do sistema:

`sudo lynis audit system`

- Executa uma auditoria de segurança de um Dockerfile:

`sudo lynis audit dockerfile {{caminho/para/dockerfile}}`
