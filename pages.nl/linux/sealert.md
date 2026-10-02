# sealert

> Analyseer en leg SELinux AVC-weigeringsberichten uit.
> Onderdeel van het `setroubleshoot-server` pakket.
> Zie ook: `audit2why`, `ausearch`, `audit2allow`.
> Meer informatie: <https://manned.org/sealert>.

- Analyseer alle recente SELinux-weigeringen:

`sudo sealert {{[-a|--analyze]}} {{/var/log/audit/audit.log}}`

- Analyseer een specifieke waarschuwings-ID uit systeemlogs:

`sudo sealert {{[-l|--lookupid]}} {{waarschuwings_id}}`

- Toon een samenvatting van recente SELinux-waarschuwingen:

`sudo sealert {{[-b|--browser]}}`

- Monitor de auditlog in real-time op nieuwe waarschuwingen:

`sudo tail {{[-f|--follow]}} {{/var/log/audit/audit.log}} | sealert {{[-l|--lookupid]}} -`
