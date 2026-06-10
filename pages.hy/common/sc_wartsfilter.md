# sc_wartsfilter

> Ընտրեք որոշակի գրառումներ `.warts` ֆայլից:.
> Լրացուցիչ տեղեկություններ. <https://www.caida.org/catalog/software/scamper/>:.

- Զտեք բոլոր տվյալների գրառումները, որոնք ունեին հատուկ նպատակակետեր և գրեք դրանք առանձին ֆայլում.:

`sc_wartsfilter -i {{path/to/input.warts}} -o {{path/to/output.warts}} -a {{192.0.2.5}} -a {{192.0.2.6}}`

- Զտեք բոլոր գրառումները, որոնք ունեին որոշակի ուղղություններ նախածանցում և գրեք դրանք առանձին ֆայլում.:

`sc_wartsfilter -i {{path/to/input.warts}} -o {{path/to/output.warts}} -a {{2001:db8::/32}}`

- Զտեք բոլոր գրառումները, որոնք օգտագործում են որոշակի գործողություն և թողարկեք դրանք որպես JSON:

`sc_wartsfilter -i {{path/to/input.warts}} -t {{ping}} | sc_warts2json`
