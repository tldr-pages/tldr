# gio trash

> 파일을 휴지통으로 이동합니다.
> GNOME에서 휴지통을 관리하는 데 사용됩니다.
> 더 많은 정보: <https://manned.org/gio.1>.

- 특정 파일을 휴지통으로 이동:

`gio trash {{경로/대상/파일_또는_폴더1 경로/대상/파일_또는_폴더2 ...}}`

- 휴지통 항목 나열:

`gio trash --list`

- ID를 사용하여 휴지통에서 특정 항목 복원:

`gio trash trash://{{id}}`
