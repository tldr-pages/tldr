# pngcrush

> PNG սեղմման կոմունալ:.
> Լրացուցիչ տեղեկություններ. <https://pmt.sourceforge.io/pngcrush/>:.

- Կոմպրես PNG ֆայլ.:

`pngcrush {{in.png}} {{out.png}}`

- Սեղմեք բոլոր PNG-ները և թողարկեք դրանք նշված գրացուցակում.:

`pngcrush -d {{path/to/output}} *.png`

- Սեղմեք PNG ֆայլը բոլոր 114 հասանելի ալգորիթմներով և ընտրեք լավագույն արդյունքը.:

`pngcrush -rem allb -brute -reduce {{in.png}} {{out.png}}`
