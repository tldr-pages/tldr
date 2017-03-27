# logwatch

> Analyzes and summarizes system logs.

- Analyze yesterday's logs in medium detail:

`logwatch --range yesterday --detail med`

- Get the summarized login information for the last 3 weeks:

`logwatch --range 'since 3 weeks ago' --detail low --service pam_unix `
