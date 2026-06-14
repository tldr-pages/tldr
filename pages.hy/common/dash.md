# գծիկ

> Debian Almquist Shell, `sh`-ի ժամանակակից, POSIX-ին համապատասխանող ներդրում (անհամատեղելի Bash-ին):.
> Լրացուցիչ տեղեկություններ. <https://manned.org/dash>:.

- Սկսեք ինտերակտիվ shell նստաշրջան.:

`dash`

- Կատարեք հատուկ [c] հրամաններ.:

`dash -c "{{echo 'dash is executed'}}"`

- Կատարել կոնկրետ սցենար.:

`dash {{path/to/script.sh}}`

- Ստուգեք հատուկ սցենար շարահյուսական սխալների համար.:

`dash -n {{path/to/script.sh}}`

- Յուրաքանչյուր հրամանը տպելիս կատարեք որոշակի սցենար, նախքան այն կատարելը.:

`dash -x {{path/to/script.sh}}`

- Կատարեք կոնկրետ սցենար և կանգ առեք առաջին [e] սխալի վրա.:

`dash -e {{path/to/script.sh}}`

- Կատարեք հատուկ հրամաններ `stdin`-ից.:

`{{echo "echo 'dash is executed'"}} | dash`
