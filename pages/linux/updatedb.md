# updatedb

> Creates or updates the database used by locate

> It usually runs daily by cron to update the default database

- Refreshes database content - required if you added new files since last time `updatedb` ran:

`sudo updatedb`

- Display file path names as soon as they are found:

`sudo updatedb --verbose`
