# բաժակ մերժել

> Մերժել տպիչներին ուղարկված աշխատանքները:.
> Նշում. նպատակակետը կոչվում է տպիչ կամ տպիչների դաս:.
> Տես նաև՝ `cupsaccept`, `cupsenable`, `cupsdisable`, `lpstat`:.
> Լրացուցիչ տեղեկություններ. <https://www.cups.org/doc/man-cupsaccept.html>:.

- Մերժել տպման աշխատանքները նշված ուղղություններով.:

`cupsreject {{destination1 destination2 ...}}`

- Նշեք այլ սերվեր.:

`cupsreject -h {{server}} {{destination1 destination2 ...}}`

- Նշեք պատճառի տողը («Պատճառը անհայտ է» լռելյայն).:

`cupsreject -r {{reason}} {{destination1 destination2 ...}}`
