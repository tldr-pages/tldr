#զեկ

> Պասիվ ցանցային տրաֆիկի անալիզատոր:.
> Ցանկացած ելքային և մատյան ֆայլ կպահվի ընթացիկ աշխատանքային գրացուցակում:.
> Լրացուցիչ տեղեկություններ. <https://docs.zeek.org/en/lts/quickstart.html#zeek-as-a-command-line-utility>:.

- Վերլուծեք ուղիղ երթևեկությունը ցանցային ինտերֆեյսից.:

`sudo zeek --iface {{interface}}`

- Վերլուծեք ուղիղ երթևեկությունը ցանցային ինտերֆեյսից և բեռնեք հատուկ սկրիպտներ.:

`sudo zeek --iface {{interface}} {{script1 script2 ...}}`

- Վերլուծեք ուղիղ երթևեկությունը ցանցային ինտերֆեյսից՝ առանց որևէ սցենար բեռնելու.:

`sudo zeek --bare-mode --iface {{interface}}`

- Վերլուծեք ուղիղ երթևեկությունը ցանցային ինտերֆեյսից՝ կիրառելով `tcpdump` զտիչ.:

`sudo zeek --filter {{path/to/filter}} --iface {{interface}}`

- Վերլուծեք ուղիղ երթևեկությունը ցանցային ինտերֆեյսից՝ օգտագործելով պահակային ժամանակաչափ.:

`sudo zeek --watchdog --iface {{interface}}`

- Վերլուծեք տրաֆիկը PCAP ֆայլից.:

`zeek --readfile {{path/to/file.trace}}`
