# hdparm

> get/set SATA/IDE device (HDD) parameters

- Request identification info of the device directly from the  drive:

`sudo hdparm -I /dev/{{device}}`

- Get Advanced Power Management feature, if the drive supports it. Possible  settings  range  from values  1  through  127 (which permit spin-down), and values 128 through 254 (which do not permit spin-down):

`sudo hdparm -B /dev/{{device}}`

- Set Advanced Power Management value:

`sudo hdparm -B {{1}} /dev/{{device}}`

- Check  the  current device power mode status:

`sudo hdparm -C /dev/{{device}}`

- Force  an  IDE drive to immediately enter the low power consumption standby mode, usually causing it to spin down:

`sudo hdparm -y /dev/{{device}}`

- Put  the  drive  into  idle  (low-power)  mode, and also set the standby (spindown) timeout for the drive:

`sudo hdparm -S {{standby timeout}} {{device}}`
