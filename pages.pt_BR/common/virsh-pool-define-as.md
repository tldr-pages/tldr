# virsh pool-define-as

> Cria um arquivo de configuração em `/etc/libvirt/storage` para um pool de armazenamento persistente de máquina virtual a partir dos argumentos fornecidos.
> Veja também: `virsh`, `virsh-pool-build`, `virsh-pool-start`.
> Mais informações: <https://manned.org/virsh>.

- Criar o arquivo de configuração para um pool de armazenamento chamado pool_name usando `/var/vms` como o sistema de armazenamento subjacente:

`virsh pool-define-as --name {{nome_do_pool}} --type {{dir}} --target {{/var/vms}}`
