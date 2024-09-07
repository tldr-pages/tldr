# apt-add-repository

> ควบคุมและจัดการที่อยู่ของคลัง APT.
> ข้อมูลเพิ่มเติม: <https://manpages.debian.org/latest/software-properties-common/apt-add-repository.1.html>

- เพิ่มที่หมายของคลัง APT:

`apt-add-repository {{ที่อยู่จำเพาะของคลัง}}`

- ลบคลัง APT:

`apt-add-repository --remove {{ที่อยู่จำเพาะของคลัง}}`

- อัพเดตข้อมูลแคชหลังจากเพิ่มคลัง APT:

`apt-add-repository --update {{ที่อยู่จำเพาะของคลัง}}`

- อนุญาตให้เข้าถึงซอรส์โค้ดของโปรแกรมในคลัง:

`apt-add-repository --enable-source {{ที่อยู่จำเพาะของคลัง}}`
