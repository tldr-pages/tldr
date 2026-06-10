# zip2john

> Քաղեք գաղտնաբառի հեշերը Zip արխիվներից՝ John the Ripper գաղտնաբառի կոտրիչով օգտագործելու համար:.
> Սա օգտակար գործիք է, որը սովորաբար տեղադրվում է որպես John the Ripper տեղադրման մաս:.
> Լրացուցիչ տեղեկություններ. <https://www.openwall.com/john/>:.

- Արխիվից հանեք գաղտնաբառի հեշը՝ թվարկելով արխիվի բոլոր ֆայլերը.:

`zip2john {{path/to/file.zip}}`

- Արտահանեք գաղտնաբառի հեշը՝ օգտագործելով [o] միայն որոշակի սեղմված ֆայլ.:

`zip2john -o {{path/to/compressed_file}} {{path/to/file.zip}}`

- Արտահանեք գաղտնաբառի հեշը սեղմված ֆայլից կոնկրետ ֆայլ (John the Ripper-ի հետ օգտագործելու համար).:

`zip2john -o {{path/to/compressed_file}} {{path/to/file.zip}} > {{file.hash}}`
