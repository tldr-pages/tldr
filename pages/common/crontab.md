# crontab

> Schedule cron jobs to run on a time interval for the current user.

- Edit the crontab file for the current user:

`crontab -e`

- View a list of existing cron jobs for current user:

`crontab -l`

- Remove all cron jobs for the current user:

`crontab -r`

- Configuration file:

```
# ┌───────────── min (0 - 59)
# │ ┌────────────── hour (0 - 23)
# │ │ ┌─────────────── day of month (1 - 31)
# │ │ │ ┌──────────────── month (1 - 12)
# │ │ │ │ ┌───────────────── day of week (0 - 6) (0 to 6 are Sunday to Saturday, or use names; 7 is Sunday, the same as 0)
# │ │ │ │ │
# │ │ │ │ │
# * * * * *  command to execute
```
