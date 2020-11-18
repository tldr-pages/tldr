# crontab

> Schedule cron jobs to run on a time interval for the current user.
> Job definition format: "(min) (hour) (day_of_month) (month) (day_of_week) command_to_execute".

- Edit the crontab file for the current user:

`crontab -e`

- Edit the crontab file for a specific user:

`sudo crontab -e -u {{user}}`

- Replace the current crontab with the contents of the given file:

`crontab {{path/to/file}}`

- View a list of existing cron jobs for current user:

`crontab -l`

- Remove all cron jobs for the current user:

`crontab -r`

- Sample job which runs at 10:00 every day (* means any value):

`0 10 * * * {{command_to_execute}}`

- Sample job which runs every minute on the 3rd of April:

`* * 3 Apr * {{command_to_execute}}`

- Sample job which runs a certain script at 02:30 every Friday:

`30 2 * * Fri {{/absolute/path/to/script.sh}}`
