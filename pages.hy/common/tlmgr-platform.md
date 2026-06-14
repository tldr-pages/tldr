# tlmgr հարթակ

> Կառավարեք TeX Live հարթակները:.
> Լրացուցիչ տեղեկություններ. <https://www.tug.org/texlive/doc/tlmgr.html#platform>:.

- Թվարկեք բոլոր հասանելի հարթակները փաթեթի պահոցում.:

`tlmgr {{[arch|platform]}} list`

- Ավելացրեք գործարկվողները կոնկրետ հարթակի համար.:

`sudo tlmgr {{[arch|platform]}} add {{platform}}`

- Հեռացրեք գործարկվողները կոնկրետ հարթակի համար.:

`sudo tlmgr {{[arch|platform]}} remove {{platform}}`

- Ավտոմատ հայտնաբերել և անցնել ընթացիկ հարթակ.:

`sudo tlmgr {{[arch|platform]}} set auto`

- Անցում դեպի կոնկրետ հարթակ.:

`sudo tlmgr {{[arch|platform]}} set {{platform}}`
