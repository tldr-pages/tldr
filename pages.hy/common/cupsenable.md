# բաժակապնակ

> Սկսեք տպիչներ և դասեր:.
> Նշում. նպատակակետը կոչվում է տպիչ կամ տպիչների դաս:.
> Տես նաև՝ `cupsdisable`, `cupsaccept`, `cupsreject`, `lpstat`:.
> Լրացուցիչ տեղեկություններ. <https://www.cups.org/doc/man-cupsenable.html>:.

- Սկսեք մեկ կամ մի քանի նպատակակետ(ներ).:

`cupsenable {{destination1 destination2 ...}}`

- Վերսկսել նպատակակետի առկախ աշխատանքների տպագրությունը (օգտագործել `cupsdisable`-ից հետո `--hold`-ով):

`cupsenable --release {{destination}}`

- Չեղարկել նշված նպատակակետ(ներ)ի բոլոր աշխատանքները.:

`cupsenable -c {{destination1 destination2 ...}}`
