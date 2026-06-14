#հատկ

> Անձնական ինտերնետ հասանելիության գործիք՝ առևտրային VPN մատակարար:.
> Լրացուցիչ տեղեկություններ. <https://helpdesk.privateinternetaccess.com/kb/articles/pia-desktop-command-line-interface-2>:.

- Մուտք գործեք մասնավոր ինտերնետ հասանելիություն.:

`piactl login {{path/to/login_file}}`

- Միացեք մասնավոր ինտերնետ հասանելիությանը.:

`piactl connect`

- Անջատեք մասնավոր ինտերնետ հասանելիությունից.:

`piactl disconnect`

- Միացնել կամ անջատել մասնավոր ինտերնետ հասանելիության դեյմոնը հետին պլանում.:

`piactl background {{enable|disable}}`

- Թվարկեք բոլոր հասանելի VPN տարածաշրջանները.:

`piactl get regions`

- Ցուցադրել ընթացիկ VPN տարածաշրջանը.:

`piactl get region`

- Սահմանեք ձեր VPN տարածաշրջանը.:

`piactl set region {{region}}`

- Դուրս գալ մասնավոր ինտերնետ հասանելիությունից.:

`piactl logout`
