# crontab

> Schedule cron jobs to run on a time interval for the current user.
> More information: <https://manned.org/crontab>.

- [e]dit the crontab file for the current user:

`crontab -e`

- [e]dit the crontab file for a specific [u]ser:

`sudo crontab -e -u {{user}}`

- Replace the current crontab with the contents of the given file:

`crontab {{path/to/file}}`

- [l]ist existing cron jobs for the current user:

`crontab -l`

- [r]emove all cron jobs for the current user:

`crontab -r`

- Sample cron job which runs at 10:00 every day (* means any value):

`0 10 * * * {{command_to_execute}}`

- Sample cron job which runs a command every 10 minutes:

`*/10 * * * * {{command_to_execute}}`

- Sample cron job which runs a certain script at 02:30 every Friday:

`30 2 * * Fri /{{path/to/script.sh}}`
