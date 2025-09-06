# csshX

> Ferramenta de Cluster SSH para macOS.
> Mais informações: <https://github.com/brockgr/csshx>.

- Conecta a vários hosts:

`csshX {{nomedohost1}} {{nomedohost2}}`

- Conecta a vários hosts com uma determinada chave SSH:

`csshX {{user@nomedohost1}} {{user@nomedohost2}} --ssh_args "-i {{caminho/para/ssh_key.pem}}"`

- Conecta a um cluster predefinido em `/etc/clusters`:

`csshX cluster1`
