# yum

> Gerenciador de pacotes utilitário para RHEL, Fedora e CentOS (para outras versões).
> Mais informações: <https://manned.org/yum>.

- Instalar um novo pacote:

`yum install {{package}}`

- Instalar um novo pacote e assumir sim para todas as questões (também funciona com atualizações, ótimo para atualizações automáticas):

`yum -y install {{package}}`

- Localizar o pacote que providência um comando particular:

`yum provides {{command}}`

- Remover um pacote:

`yum remove {{package}}`

- Exibir atualizações disponíveis para pacotes instalados:

`yum check-update`

- Atualizar pacotes instalados para as novas versões disponíveis:

`yum upgrade`
