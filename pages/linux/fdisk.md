# fdisk
> Manipulate disk partition table.

`fdisk -l {{device}}`
- List  the  partition  tables for the sda disk and then exit.If no devices are given,
              those mentioned in /proc/partitions (if that exists) are used:
              device is usually /dev/sda or /dev/sdb or so. For example: 
              #fdisk  -l /dev/sda will show the partition tables for sda disk.

`fdisk -s {{device}}`
- Print the size (in blocks) of device partition,such as /dev/sda1

`fdisk {{devices}}`
- Create/remove/change partitions in the device.Serveral commands can be list.for example:
#fdisk /dev/sda ,which will lead into command line for create/remove/ and so on actions for sda.

      `m`
      print the help menu
      
      `n`
      add new partition, the new partition can be craeted if you type the command as the tips
      
      `l`
      list the known partition types,such as NTFS,GPT,EFI or so.
      
      `p`
      print the partition table, the function is as same as fdisk /dev/sda -l
      
      `w`
      write table to disk and exit. The command can be typed after the new partition is created.
      
      `d`
      delete a partition    

`fdisk -h`
- Print help and then exit
