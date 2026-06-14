# distccd

> Server daemon distcc բաշխված կոմպիլյատորի համար:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/distccd>:.

- Սկսեք դևոն լռելյայն կարգավորումներով.:

`distccd --daemon`

- Սկսեք դևոն՝ ընդունելով կապեր IPv4 մասնավոր ցանցի տիրույթներից.:

`distccd --daemon --allow-private`

- Սկսեք դևոն՝ ընդունելով կապեր որոշակի ցանցային հասցեից կամ հասցեների տիրույթից.:

`distccd --daemon {{[-a|--allow]}} {{ip_address|network_prefix}}`

- Սկսեք դևոն իջեցված առաջնահերթությամբ, որը կարող է միաժամանակ կատարել առավելագույնը 4 առաջադրանք.:

`distccd --daemon {{[-j|--jobs]}} {{4}} {{[-N|--nice]}} {{5}}`

- Սկսեք դևոն և գրանցեք այն mDNS/DNS-SD (Zeroconf) միջոցով:

`distccd --daemon --zeroconf`
