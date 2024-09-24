# dkms

> Um framework que permite recompilação dinâmica de modulos do kernel.
> Mais informações: <https://github.com/dell/dkms>.

- Lista os módulos instalados atualmente:

`dkms status`

- Recompila todos os módulos para o kernel que está rodando atualmente:

`dkms autoinstall`

- Instala a versão 1.2.1 do módulo acpi_call para o kernel que está rodando atualmente:

`dkms install -m {{acpi_call}} -v {{1.2.1}}`

- Remove a versão 1.2.1 do módulo acpi_call de todos os kernels:

`dkms remove -m {{acpi_call}} -v {{1.2.1}} --all`
