# matchpathcon

> Zoek de persistente SELinux-beveiligingscontextinstelling van een pad op.
> Zie ook: `semanage fcontext`, `secon`, `chcon`, `restorecon`.
> Meer informatie: <https://manned.org/matchpathcon.8>.

- Zoek de persistente beveiligingscontextinstelling van een absoluut pad op:

`matchpathcon /{{pad/naar/bestand}}`

- Beperk het opzoeken tot instellingen voor een specifiek bestandstype:

`matchpathcon -m {{file|dir|pipe|chr_file|blk_file|lnk_file|sock_file}} /{{pad/naar/bestand}}`

- [V]erifieer dat de persistente en huidige beveiligingscontext van een pad overeenkomen:

`matchpathcon -V /{{pad/naar/bestand}}`
