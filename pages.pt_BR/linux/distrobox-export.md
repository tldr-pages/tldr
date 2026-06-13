# distrobox-export

> Exportar um aplicativo/serviço/binário do contêiner para o sistema operacional host.
> Subcomando de `distrobox`.
> Veja também: `distrobox`.
> Mais informações: <https://distrobox.it/usage/distrobox-export/>.

- Exporta um aplicativo do contêiner para o host (a entrada e o ícone do aplicativo aparecerão na lista de aplicativos do seu sistema host):

`distrobox-export {{[-a|--app]}} {{nome_do_pacote}} {{[-ef|--extra-flags]}} "--foreground"`

- Exporta um binário do contêiner para o host:

`distrobox-export {{[-b|--bin]}} {{caminho/para/binário}} {{[-ep|--export-path]}} {{caminho/para/binário_no_host}}`

- Exporta um binário do contêiner para o host (por exemplo, `$HOME/.local/bin`):

`distrobox-export {{[-b|--bin]}} {{caminho/para/binário}} {{[-ep|--export-path]}} {{caminho/de/exportação}}`

- Exporta um serviço do contêiner para o host (`--sudo` executará o serviço como root dentro do contêiner):

`distrobox-export --service {{pacote}} {{[-ef|--extra-flags]}} "--allow-newer-config" {{[-S|--sudo]}}`

- Desexportar/deletar um aplicativo exportado:

`distrobox-export {{[-a|--app]}} {{pacote}} {{[-d|--delete]}}`
