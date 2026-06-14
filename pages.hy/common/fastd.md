#պաս

> VPN դեյմոն.
> Աշխատում է 2-րդ կամ 3-րդ շերտի վրա, աջակցում է գաղտնագրման տարբեր մեթոդներ, որոնք օգտագործվում են Freifunk-ի կողմից:.
> Տես նաև՝ `ivpn`, `mozillavpn`, `mullvad`, `warp-cli`:.
> Լրացուցիչ տեղեկություններ. <https://fastd.readthedocs.io/en/stable/>:.

- Սկսեք `fastd`-ը որոշակի կազմաձևման ֆայլով.:

`fastd {{[-c|--config]}} {{path/to/fastd.conf}}`

- Սկսեք Layer 3 VPN-ը 1400 MTU-ով, բեռնելով մնացած կազմաձևման պարամետրերը ֆայլից.:

`fastd {{[-m|--mode]}} {{tap}} {{[-M|--mtu]}} {{1400}} {{[-c|--config]}} {{path/to/fastd.conf}}`

- Վավերացրեք կազմաձևման ֆայլը.:

`fastd --verify-config {{[-c|--config]}} {{path/to/fastd.conf}}`

- Ստեղծեք նոր բանալիների զույգ.:

`fastd --generate-key`

- Ցուցադրել հանրային բանալին մասնավոր բանալիի համար կազմաձևման ֆայլում.:

`fastd --show-key {{[-c|--config]}} {{path/to/fastd.conf}}`

- Ցուցադրման տարբերակը:

`fastd {{[-v|--version]}}`
