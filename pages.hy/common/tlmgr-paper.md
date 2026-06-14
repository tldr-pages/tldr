# tlmgr թուղթ

> Կառավարեք TeX Live տեղադրման թղթի չափի ընտրանքները:.
> Լրացուցիչ տեղեկություններ. <https://www.tug.org/texlive/doc/tlmgr.html#paper>:.

- Ցույց տալ բոլոր TeX Live ծրագրերի կողմից օգտագործվող լռելյայն թղթի չափը.:

`tlmgr paper`

- Բոլոր TeX Live ծրագրերի համար թղթի լռելյայն չափը սահմանեք A4:

`sudo tlmgr paper {{a4}}`

- Ցույց տալ թղթի լռելյայն չափը, որն օգտագործվում է հատուկ TeX Live ծրագրի կողմից.:

`tlmgr {{pdftex}} paper`

- Սահմանեք թղթի լռելյայն չափը կոնկրետ TeX Live ծրագրի համար A4:

`sudo tlmgr {{pdftex}} paper {{a4}}`

- Թվարկեք թղթի բոլոր հասանելի չափերը հատուկ TeX Live ծրագրի համար.:

`tlmgr {{pdftex}} paper --list`

- Թափել լռելյայն թղթի չափը, որն օգտագործվում է բոլոր TeX Live ծրագրերի կողմից JSON ձևաչափով.:

`tlmgr paper --json`
