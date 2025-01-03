# semanage fcontext

> Beheer persistente SELinux-beveiligingscontextregels op bestanden/mappen.
> Bekijk ook: `semanage`, `matchpathcon`, `secon`, `chcon`, `restorecon`.
> Meer informatie: <https://manned.org/semanage-fcontext>.

- Toon alle bestandslabelregels:

`sudo semanage fcontext --list`

- Toon alle door de gebruiker gedefinieerde bestandslabelregels zonder koppen:

`sudo semanage fcontext --list --locallist --noheading`

- Voeg een door de gebruiker gedefinieerde regel toe die elk pad labelt dat overeenkomt met een PCRE-regex:

`sudo semanage fcontext --add --type {{samba_share_t}} {{'/mnt/share(/.*)?'}}`

- Verwijder een door de gebruiker gedefinieerde regel met behulp van zijn PCRE-regex:

`sudo semanage fcontext --delete {{'/mnt/share(/.*)?'}}`

- Herlabel een map recursief door de nieuwe regels toe te passen:

`restorecon -R -v {{pad/naar/map}}`
