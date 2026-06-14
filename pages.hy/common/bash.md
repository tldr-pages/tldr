#բաշ

> Bourne-Again SHell, `sh`-համատեղելի հրամանի տողի թարգմանիչ:.
> Տես նաև՝ `zsh`, `!`:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/bash/manual/bash.html#Invoking-Bash>:.

- Սկսեք ինտերակտիվ shell նստաշրջան.:

`bash`

- Սկսեք ինտերակտիվ կեղևի նստաշրջան առանց գործարկման կազմաձևերի բեռնման.:

`bash --norc`

- Կատարեք հատուկ [c] հրամաններ.:

`bash -c "{{echo 'bash is executed'}}"`

- Կատարել կոնկրետ սցենար.:

`bash {{path/to/script.sh}}`

- E[x]կատարեք որոշակի սկրիպտ՝ տպելով յուրաքանչյուր հրաման՝ նախքան այն կատարելը.:

`bash -x {{path/to/script.sh}}`

- Կատարեք կոնկրետ սցենար և կանգ առեք առաջին [e] սխալի վրա.:

`bash -e {{path/to/script.sh}}`

- Կատարեք հատուկ հրամաններ `stdin`-ից.:

`{{echo "echo 'bash is executed'"}} | bash`

- Սկսեք [r] սահմանափակ կեղևի նստաշրջան.:

`bash {{[-r|--restricted]}}`
