# ntfs-read.py

> NTFS 볼륨에서 파일을 탐색하고 추출할 수 있는 읽기 전용 NTFS 탐색 도구.
> Impacket 도구의 일부.
> 더 많은 정보: <https://github.com/fortra/impacket>.

- NTFS 볼륨 탐색 시작 (예: `C:\.\\` 또는 `/dev/disk1s1`):

`ntfs-read.py {{볼륨}}`

- NTFS 볼륨에서 특정 파일 추출 (예: `\windows\system32\config\sam`):

`ntfs-read.py -extract {{\windows\system32\config\sam}} {{볼륨}}`

- 디버그 출력 활성화:

`ntfs-read.py -debug {{볼륨}}`

- 도움말 표시:

`ntfs-read.py --help`
