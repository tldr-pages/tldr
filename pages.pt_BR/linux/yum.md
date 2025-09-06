# yum

> Gerenciador de pacotes utilitário para RHEL, Fedora e CentOS (para outras versões).
> Mais informações: <https://manned.org/yum>.

- Instala um novo pacote:

`yum install {{package}}`

- Instala um novo pacote assumindo sim para todas as perguntas (também funciona com atualizações, ótimo para atualizações automáticas):

`yum -y install {{package}}`

- Localiza o pacote que providência um comando particular:

`yum provides {{command}}`

- Remove um pacote:

`yum remove {{package}}`

- Exibe atualizações disponíveis para pacotes instalados:

`yum check-update`

- Atualiza pacotes instalados para as novas versões disponíveis:

`yum upgrade`
