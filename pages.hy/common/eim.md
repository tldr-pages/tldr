#էիմ

> Տեղադրեք և կառավարեք ESP-IDF-ը:.
> Լրացուցիչ տեղեկություններ. <https://docs.espressif.com/projects/idf-im-ui/en/latest/cli_commands.html>:.

- Տեղադրեք կանխադրված (վերջին) ESP-IDF տարբերակը լռելյայն վայրում (`C:\esp` Windows-ում և `~/.espressif` POSIX համակարգերում):

`eim install`

- Տեղադրեք հատուկ ESP-IDF տարբերակ.:

`eim install {{[-i|--idf-versions]}} {{v5.3.2}}`

- Գործարկեք ինտերակտիվ, առաջնորդվող տեղադրման հրաշագործը.:

`eim wizard`

- Տեղադրեք հատուկ տարբերակ հատուկ ուղու վրա՝ ստիպելով ինտերակտիվ ռեժիմը (ընտրություններ հուշելու համար).:

`eim install {{[-i|--idf-versions]}} {{v5.3.2}} {{[-p|--path]}} {{/opt/esp-idf}} {{[-n|--non-interactive]}} false`

- Թվարկեք բոլոր ներկայումս տեղադրված ESP-IDF տարբերակները.:

`eim list`

- Հեռացրեք հատուկ տեղադրված ESP-IDF տարբերակը.:

`eim remove {{v5.3.2}}`

- Տեղադրեք առանց գլխի ռեժիմում՝ օգտագործելով TOML կազմաձևման ֆայլում սահմանված բոլոր տարբերակները.:

`eim install {{[-c|--config]}} {{path/to/config.toml}}`

- Տեղադրեք անցանց՝ օգտագործելով նախապես ներբեռնված արխիվային ֆայլը.:

`eim install --use-local-archive {{path/to/archive.zst}}`
