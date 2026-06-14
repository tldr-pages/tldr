# tlmgr gui

> Սկսեք գրաֆիկական ինտերֆեյս `tlmgr`-ի համար:.
> `tlmgr gui` կախված է `perl-tk` փաթեթից, որը պետք է ձեռքով տեղադրվի:.
> Լրացուցիչ տեղեկություններ. <https://www.tug.org/texlive/doc/tlmgr.html#gui>:.

- Սկսեք GUI `tlmgr`-ի համար՝:

`sudo tlmgr gui`

- Սկսեք GUI՝ նշելով ֆոնի գույնը.:

`sudo tlmgr gui -background "{{#f39bc3}}"`

- Սկսեք GUI՝ նշելով առաջին պլանի գույնը.:

`sudo tlmgr gui -foreground "{{#0ef3bd}}"`

- Սկսեք GUI՝ նշելով տառատեսակը և տառաչափը.:

`sudo tlmgr gui -font "{{helvetica 18}}"`

- Սկսեք GUI սահմանելով որոշակի երկրաչափություն.:

`sudo tlmgr gui -geometry {{width}}x{{height}}-{{xpos}}+{{ypos}}`

- Սկսեք GUI՝ անցնելով կամայական X ռեսուրսների տողը.:

`sudo tlmgr gui -xrm {{xresource}}`
