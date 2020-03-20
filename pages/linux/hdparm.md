# hdparm

> Get and set SATA and IDE hard drive parameters.

- Request identification info of the device directly from the drive:

`sudo hdparm -I /dev/{{device}}`

- Get Advanced Power Management feature, if the drive supports it:

`sudo hdparm -B /dev/{{device}}`

- Set Advanced Power Management value. Values 1-127 permit spin-down, and values 128-254 do not:

`sudo hdparm -B {{1}} /dev/{{device}}`

- Check the current device power mode status:

`sudo hdparm -C /dev/{{device}}`

- Force a drive to immediately enter the standby mode, usually causing it to spin down:

`sudo hdparm -y /dev/{{device}}`

- Put the drive into idle (low-power) mode, and also set its standby timeout:

`sudo hdparm -S {{standby timeout}} {{device}}`
