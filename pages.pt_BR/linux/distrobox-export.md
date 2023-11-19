# distrobox-export

> Exportar um aplicativo/serviço/binário do contêiner para o sistema operacional host.
> Subcomando de `distrobox`. Veja também: `tldr distrobox`.
> Mais informações: <https://distrobox.it/usage/distrobox-export>.

- Exportar um aplicativo do contêiner para o host (a entrada e o ícone do aplicativo aparecerão na lista de aplicativos do seu sistema host):

`distrobox-export --app {{nome_do_pacote}} --extra-flags "--foreground"`

- Exportar um binário do contêiner para o host:

`distrobox-export --bin {{caminho/para/binário}} --export-path {{caminho/para/binário_no_host}}`

- Exportar um binário do contêiner para o host (por exemplo, `$HOME/.local/bin`):

`distrobox-export --bin {{caminho/para/binário}} --export-path {{caminho/de/exportação}}`

- Exportar um serviço do contêiner para o host (`--sudo` executará o serviço como root dentro do contêiner):

`distrobox-export --service {{pacote}} --extra-flags "--allow-newer-config" --sudo`

- Desexportar/deletar um aplicativo exportado:

`distrobox-export --app {{pacote}} --delete`
