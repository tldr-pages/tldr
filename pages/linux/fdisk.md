# fdisk

> Manipulate disk partition table.



`fdisk -l {{device}}`

- List  the  partition  tables for the sda disk and then exit.If no devices are given,
              those mentioned in /proc/partitions (if that exists) are used:
              device is usually /dev/sda or /dev/sdb or so.

`fdisk -s /dev/sda1`

- Print the size (in blocks) of /dev/sda1 partition:

`fdisk {{devices}}`

- Create/remove/change partitions in the device.Serveral commands can be list.

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
