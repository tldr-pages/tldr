# սպասել4x tcp

> Սպասեք, մինչև TCP պորտ(ներ)ը հասանելի դառնան:.
> Լրացուցիչ տեղեկություններ. <https://github.com/wait4x/wait4x>:.

- Սպասեք, մինչև TCP պորտը հասանելի դառնա.:

`wait4x tcp {{localhost:8080}}`

- Սպասեք մի նավահանգստի որոշակի ժամանակի ավարտով.:

`wait4x tcp {{localhost:3306}} --timeout {{60s}}`

- Սպասեք, որ նավահանգիստը դառնա անվճար (շրջված ստուգում).:

`wait4x tcp {{localhost:8080}} --invert-check`

- Սպասեք մի քանի նավահանգիստների զուգահեռ.:

`wait4x tcp {{localhost:3306 localhost:6379 ...}}`

- Գործարկեք հրամանը, երբ նավահանգիստը հասանելի կդառնա.:

`wait4x tcp {{localhost:3306}} -- {{path/to/script.sh}}`

- Սպասեք էքսպոնենցիալ հետընթացով.:

`wait4x tcp {{localhost:8080}} --backoff-policy exponential --backoff-exponential-max-interval {{30s}}`
