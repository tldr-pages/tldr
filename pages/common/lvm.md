\# lvm



> Manage logical volumes, volume groups, and physical volumes in Linux.

> The `lvm` command provides a unified interface for managing logical volume operations.

> More information: <https://man7.org/linux/man-pages/man8/lvm.8.html>.



\- Display LVM version and configuration details:



`lvm version`



\- Show all logical volumes:



`lvm lvs`



\- Show all volume groups:



`lvm vgs`



\- Show all physical volumes:



`lvm pvs`



\- Create a new logical volume of 10 GB in a specific volume group:



`lvm lvcreate -L {{10G}} -n {{logical\_volume\_name}} {{volume\_group\_name}}`



\- Remove a logical volume:



`lvm lvremove {{volume\_group\_name}}/{{logical\_volume\_name}}`



\- Extend a logical volume by 5 GB:



`lvm lvextend -L +{{5G}} {{volume\_group\_name}}/{{logical\_volume\_name}}`



\- Reduce a logical volume after unmounting it:



`lvm lvreduce -L -{{2G}} {{volume\_group\_name}}/{{logical\_volume\_name}}`



