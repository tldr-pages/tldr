# MOUNT

> 호스트의 디렉터리/드라이브/이미지를 가상 DOS 드라이브로 마운트하는 명령어.
> 더 많은 정보: <https://www.dosbox.com/wiki/MOUNT>.

- 현재 디렉터리를 C 드라이브로 마운트:

`MOUNT C .`

- 특정 디렉터리를 C 드라이브로 마운트:

`MOUNT C {{C:\경로\대상\디렉터리}}`

- 사용 가능한 공간의 제한 설정 (MB 단위로):

`MOUNT C {{C:\경로\대상\디렉터리}} -freesize {{1024}}`

- 플로피 드라이브 마운트:

`MOUNT A {{A:\}} -t floppy`

- CD-ROM 드라이브 마운트:

`MOUNT D {{D:\}} -t cdrom`

- 추가 옵션을 사용해 CD 마운트:

`MOUNT D {{D:\}} -t cdrom -usecd {{0}} -ioctl`

- 드라이브 마운트 해제:

`MOUNT -u {{C}}`
