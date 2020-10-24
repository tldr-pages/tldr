# logwatch

> Summarizes many different logs for common services (e.g., apache, pam_unix, sshd, etc.) in a single report.

- Analyze logs for a range of dates at certain level of detail:

`logwatch --range {{yesterday|today|all|help}} --detail {{low|medium|others}}'`

- Restrict report to only include information for a selected service:

`logwatch --range {{all}} --service {{apache|pam_unix|etc}}`
