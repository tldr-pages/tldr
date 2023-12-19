# dnf

> Gerenciador de pacotes das distribuições baseadas em RHEL (substituto do yum).
> Mais informações: <https://dnf.readthedocs.io>.

- Instala um novo pacote:

`sudo dnf install {{nome_do_pacote}}`

- Instala um novo pacote e responder sim para todas as questões:

`sudo dnf -y install {{nome_do_pacote}}`

- Remove um pacote:

`sudo dnf remove {{nome_do_pacote}}`

- Atualiza todos os pacotes instalados para as versões mais recentes:

`sudo dnf upgrade`
