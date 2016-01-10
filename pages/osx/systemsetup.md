# systemsetup

> Configure System Preferences machine settings.

- Enable remote login (SSH):

`systemsetup -setremotelogin on`

- Specify TimeZone, NTP Server and enable network time:

`systemsetup -settimezone {{US/Pacific}}`
`systemsetup -setnetworktimeserver {{us.pool.ntp.org}}`
`systemsetup -setusingnetworktime on`

- Make the machine never sleep; restart on freeze & power failure:

`systemsetup -setsleep off`
`systemsetup -setrestartpowerfailure on`
`systemsetup -setrestartfreeze on`

- List valid startup disks, specify a new startup disk:

`systemsetup -liststartupdisks`
`systemsetup -setstartupdisk {{path}}`
