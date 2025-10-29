\# lvm



> Manage Logical Volume Manager (LVM) volumes in Linux.

> More information: <https://man7.org/linux/man-pages/man8/lvm.8.html>.



\- Display all logical volumes:



`lvm lvs`



\- Display all volume groups:



`lvm vgs`



\- Display all physical volumes:



`lvm pvs`



\- Create a new logical volume:



`lvm lvcreate -L {{size}} -n {{logical\_volume\_name}} {{volume\_group\_name}}`



\- Extend a logical volume by a specific size:



`lvm lvextend -L +{{size}} {{logical\_volume\_path}}`



\- Remove a logical volume:



`lvm lvremove {{logical\_volume\_path}}`



