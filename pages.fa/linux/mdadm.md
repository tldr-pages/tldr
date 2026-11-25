# mdadm

> ابزار مدیریت RAID.
> اطلاعات بیشتر: <https://manned.org/mdadm>.

- ایجاد آرایه:

`sudo mdadm --create {{/dev/md/MyRAID}} --level {{raid_level}} --raid-devices {{number_of_disks}} {{/dev/sdXN}}`

- توقف آرایه:

`sudo mdadm --stop {{/dev/md0}}`

- علامت‌گذاری دیسک به‌عنوان خراب:

`sudo mdadm --fail {{/dev/md0}} {{/dev/sdXN}}`

- حذف دیسک:

`sudo mdadm --remove {{/dev/md0}} {{/dev/sdXN}}`

- افزودن دیسک به آرایه:

`sudo mdadm --assemble {{/dev/md0}} {{/dev/sdXN}}`

- نمایش اطلاعات RAID:

`sudo mdadm --detail {{/dev/md0}}`

- بازنشانی دیسک با حذف فرادادهٔ RAID:

`sudo mdadm --zero-superblock {{/dev/sdXN}}`
