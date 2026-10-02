# gio

> 로컬 파일과 가상 파일(GVfs)을 관리.
> GNOME 기반 시스템에서 사용되는 GLib의 일부.
> 더 많은 정보: <https://manned.org/gio>.

- 기본 애플리케이션으로 파일 열기 (예: PDF, 이미지):

`gio open {{경로/대상/파일}}`

- 디렉터리의 파일 목록 표시:

`gio list {{경로/대상/디렉터리}}`

- 파일 정보 표시:

`gio info {{경로/대상/파일}}`

- 파일 복사:

`gio copy {{경로/대상/소스파일}} {{경로/대상/대상파일}}`

- 파일을 휴지통으로 이동 (복원 가능):

`gio trash {{경로/대상/파일}}`

- 휴지통 비우기:

`gio trash --empty`

- `.desktop` 파일로 애플리케이션 실행:

`gio launch {{경로/대상/파일}}.desktop`

- `.desktop` 파일을 신뢰할 수 있는 파일로 표시하여, 실행 가능하게 설정:

`gio set {{경로/대상/파일}}.desktop metadata::trusted true`
