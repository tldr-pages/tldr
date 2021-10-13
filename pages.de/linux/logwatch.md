# logwatch

> Fasst viele verschiedene Logs für gängige Dienste (z.B. Apache, pam_unix, sshd, usw.) in einem einzelnen Bericht zusammen.
> Weitere Informationen: <https://manned.org/logwatch>.

- Analysiere Logs für verschiedene Zeiträume auf einer bestimmten Detailebene:

`logwatch --range {{yesterday|today|all|help}} --detail {{low|medium|others}}'`

- Beschränkt den Bericht, um nur Informationen zu einem ausgewählten Dienst zu erhalten:

`logwatch --range {{all}} --service {{apache|pam_unix|etc}}`
