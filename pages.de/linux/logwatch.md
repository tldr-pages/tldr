# logwatch

> Fasst viele verschiedene Logs für gängige Dienste (z.B. Apache, pam_unix, sshd, usw.) in einem einzelnen Bericht zusammen.
> Weitere Informationen: <https://manned.org/logwatch>.

- Analysiere Logs für einen Zeitraum auf einer bestimmten Detailebene:

`logwatch --range {{yesterday|today|all|help}} --detail {{low|medium|others}}'`

- Beschränke den Bericht auf Informationen zu einem ausgewählten Dienst:

`logwatch --range {{all}} --service {{apache|pam_unix|etc}}`
