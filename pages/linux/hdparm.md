# hdparm

> Get and set SATA and IDE hard drive parameters.
> More information: <https://manned.org/hdparm>.

- Request the identification info of a given device:

`sudo hdparm -I /dev/{{device}}`

- Get the Advanced Power Management level:

`sudo hdparm -B /dev/{{device}}`

- Set the Advanced Power Management value (values 1-127 permit spin-down, and values 128-254 do not):

`sudo hdparm -B {{1}} /dev/{{device}}`

- Display the device's current power mode status:

`sudo hdparm -C /dev/{{device}}`

- Force a drive to immediately enter standby mode (usually causes a drive to spin down):

`sudo hdparm -y /dev/{{device}}`

- Put the drive into idle (low-power) mode, also setting its standby timeout:

`sudo hdparm -S {{standby_timeout}} {{device}}`
