# թափառաշրջիկ հավելված

> Կառավարեք Vagrant հավելվածները:.
> Տես նաև՝ `vagrant`:.
> Լրացուցիչ տեղեկություններ. <https://developer.hashicorp.com/vagrant/docs/cli/plugin>:.

- Թվարկեք ներկայումս տեղադրված բոլոր պլագինները.:

`vagrant plugin list`

- Տեղադրեք փլագին հեռավոր պահեստներից, սովորաբար RubyGems:

`vagrant plugin install {{vagrant_vbguest}}`

- Տեղադրեք plugin տեղական ֆայլի աղբյուրից.:

`vagrant plugin install {{path/to/my_plugin.gem}}`

- Թարմացրեք բոլոր տեղադրված պլագինները իրենց վերջին տարբերակին.:

`vagrant plugin update`

- Թարմացրեք հավելվածը վերջին տարբերակին.:

`vagrant plugin update {{vagrant_vbguest}}`

- Տեղահանեք հատուկ պլագին.:

`vagrant plugin uninstall {{vagrant_vbguest}}`
