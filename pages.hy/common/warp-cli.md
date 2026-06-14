# warp-cli

> Միացրեք, անջատեք և փոխարկեք միացման ռեժիմները Cloudflare-ի WARP ծառայությանը:.
> WARP-ը VPN է, որը ծածկագրում է երթևեկությունը գաղտնիության, անվտանգության և արագության համար:.
> Տես նաև՝ `fastd`, `ivpn`, `mozillavpn`, `mullvad`:.
> Լրացուցիչ տեղեկություններ. <https://developers.cloudflare.com/warp-client/>:.

- Գրանցեք ընթացիկ սարքը WARP-ում (պետք է գործարկվի մինչև առաջին միացումը).:

`warp-cli registration new`

- Ցուցադրել ընթացիկ գրանցման տվյալները.:

`warp-cli registration show`

- Միացեք WARP-ին.:

`warp-cli connect`

- Անջատեք WARP-ից.:

`warp-cli disconnect`

- Ցուցադրել WARP կապի կարգավիճակը.:

`warp-cli status`

- Ցուցադրել ընթացիկ հավելվածի կարգավորումները.:

`warp-cli settings list`

- Անցեք որոշակի ռեժիմի.:

`warp-cli mode {{warp|doh|warp+doh|dot|warp+dot|proxy|tunnel_only}}`
