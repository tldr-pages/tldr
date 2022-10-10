# apt-add-repository

> ควบคุมและจัดการที่อยู่ของคลัง apt 
> ข้อมูลเพิ่มเติม: <https://manpages.debian.org/latest/software-properties-common/apt-add-repository.1.html>.

- เพิ่มที่หมายของคลัง apt

`apt-add-repository {{repository_spec}}`

- ลบคลัง apt

`apt-add-repository --remove {{repository_spec}}`

- อัพเดตข้อมูลแคชหลังจากเพิ่มคลัง apt

`apt-add-repository --update {{repository_spec}}`

- อนุญาตให้เข้าถึงซอรส์โค้ดของโปรแกรมในคลัง

`apt-add-repository --enable-source {{repository_spec}}`
