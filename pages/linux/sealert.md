# sealert

> Analyze and explain SELinux AVC denial messages.
> Part of the `setroubleshoot-server` package.
> See also: `audit2why`, `ausearch`, `audit2allow`.
> More information: <https://manned.org/sealert>.

- Analyze all recent SELinux denials:

`sudo sealert {{[-a|--analyze]}} {{/var/log/audit/audit.log}}`

- Analyze a specific alert ID from system logs:

`sudo sealert {{[-l|--lookupid]}} {{alert_id}}`

- Display a summary of recent SELinux alerts:

`sudo sealert {{[-b|--browser]}}`

- Monitor audit log in real-time for new alerts:

`sudo tail {{[-f|--follow]}} {{/var/log/audit/audit.log}} | sealert {{[-l|--lookupid]}} -`
