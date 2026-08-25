# gio trash

> 파일을 휴지통으로 이동.
> GNOME에서 휴지통을 관리하는 데 사용됨.
> 더 많은 정보: <https://manned.org/gio>.

- 지정한 파일 또는 디렉터리를 휴지통으로 이동:

`gio trash {{경로/대상/파일_또는_디렉터리1 경로/대상/파일_또는_디렉터리2 ...}}`

- 휴지통 항목 목록 표시:

`gio trash --list`

- 휴지통 비우기:

`gio trash --empty`

- ID를 사용하여 휴지통의 항목 복원:

`gio trash trash://{{아이디}}`
