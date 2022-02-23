# wpa_supplicant

> Gerenciador de redes wireless protegidas.
> Mais informações: <https://manned.org/wpa_supplicant.1>.

- Entrar em uma rede wireless protegida:

`wpa_supplicant -i {{interface}} -c {{caminho/para/wpa_supplicant_conf.conf}}`

- Entrar em uma rede wireless protegida e executar o wpa_cli em um daemon:

`wpa_supplicant -B -i {{interface}} -c {{caminho/para/wpa_supplicant_conf.conf}}`
