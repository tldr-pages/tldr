# asnmap

> Go CLI գործիք՝ ASN տեղեկատվության օգտագործմամբ կազմակերպությունների ցանցի միջակայքերը քարտեզագրելու համար:.
> Նշում. գործիքի աշխատանքի համար պահանջվում է API բանալի ProjectDiscovery Cloud Platform-ից:.
> Լրացուցիչ տեղեկություններ. <https://github.com/projectdiscovery/asnmap#usage>:.

- Փնտրեք CIDR միջակայքերը ASN-ի համար.:

`asnmap {{[-a|-asn]}} {{AS5650}} -silent`

- Փնտրեք CIDR միջակայքերը IP հասցեի համար.:

`asnmap {{[-i|-ip]}} {{100.19.12.21}} -silent`

- Փնտրեք CIDR միջակայքերը տիրույթի համար.:

`asnmap {{[-d|-domain]}} {{example.com}} -silent`

- Որոնել CIDR միջակայքերը կազմակերպության համար.:

`asnmap -org {{GOOGLE}} -silent`

- CIDR-ի որոնումը տատանվում է թիրախների ֆայլից.:

`asnmap {{[-f|-file]}} {{path/to/targets.txt}} -silent`

- Արդյունքները JSON ձևաչափով.:

`asnmap {{[-d|-domain]}} {{facebook.com}} {{[-j|-json]}} -silent`

- Արդյունքների թողարկում CSV ձևաչափով.:

`asnmap {{[-a|-asn]}} {{AS394161}} {{[-c|-csv]}} -silent`

- Թարմացրեք asnmap-ը վերջին տարբերակին.:

`asnmap {{[-up|-update]}}`
