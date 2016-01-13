# crontab

> A crontab file contains instructions for running a command at a recurring date and time.  
> field         allowed values
> -----         --------------
> minute        0-59
> hour          0-23
> day of month  1-31
> month         1-12 (or use names: jan, feb, etc)
> day of week   0-7 (0 or 7 is Sun, or use names: mon, tue, etc)

- Run daily, at 8:05am:

`5 8 * * *`

- Run weekly, at midnight, on Mondays:

`0 * * * mon`

- Run monthly, on the first day of the month, at 2:00pm:

`0 14 1 * *`

- Run hourly, between the hours of 9:00am to 5:00pm, but only on weekdays:

`0 9-17 * * mon-fri`

- Run every 2 hours (by specifying a range with step of 2):

`0 0-23/2 * * *`
