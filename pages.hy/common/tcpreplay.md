# tcpreplay

> Կրկնել `pcap` ֆայլում պահված ցանցային տրաֆիկը:.
> Լրացուցիչ տեղեկություններ. <https://tcpreplay.appneta.com/wiki/tcpreplay-man.html>:.

- Ցուցակեք հասանելի ցանցային միջերեսները.:

`tcpreplay --listnics`

- Կրկնել երթևեկությունը դեպի ինտերֆեյս.:

`tcpreplay {{[-i|--intf1]}} {{eth0}} {{traffic.pcap}}`

- Կրկնել երթևեկությունը դեպի միջերես և `stdout`:

`tcpreplay {{[-i|--intf1]}} {{eth0}} {{[-v|--verbose]}} {{traffic.pcap}}`

- Հնարավորինս արագ վերարտադրեք տրաֆիկը ինտերֆեյսի համար.:

`tcpreplay {{[-i|--intf1]}} {{eth0}} {{[-t|--topspeed]}} {{traffic.pcap}}`

- Վերարտադրեք տրաֆիկը դեպի ինտերֆեյս տվյալ Մբիթ/վրկ արագությամբ.:

`tcpreplay {{[-i|--intf1]}} {{eth0}} {{[-M|--mbps]}} {{10}} {{traffic.pcap}}`

- Մի քանի անգամ վերարտադրեք երթևեկությունը ինտերֆեյսի համար.:

`tcpreplay {{[-i|--intf1]}} {{eth0}} {{[-l|--loop]}} {{num_times}} {{traffic.pcap}}`
