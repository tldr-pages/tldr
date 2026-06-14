# tlmgr բանալի

> Կառավարեք GPG ստեղները, որոնք օգտագործվում են TeX Live տվյալների բազաները ստուգելու համար:.
> Լրացուցիչ տեղեկություններ. <https://www.tug.org/texlive/doc/tlmgr.html#key>:.

- Թվարկեք բոլոր ստեղները TeX Live-ի համար.:

`tlmgr key list`

- Ավելացնել բանալի կոնկրետ ֆայլից.:

`sudo tlmgr key add {{path/to/key.gpg}}`

- Ավելացնել բանալի `stdin`-ից՝:

`cat {{path/to/key.gpg}} | sudo tlmgr key add -`

- Հեռացրեք հատուկ բանալի իր ID-ով.:

`sudo tlmgr key remove {{key_id}}`
