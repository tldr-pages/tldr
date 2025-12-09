# dex

> DesktopEntry Execution은 응용 프로그램 유형의 DesktopEntry 파일을 생성하고 실행하는 프로그램입니다.
> 더 많은 정보: <https://github.com/jceb/dex#dex>.

- 자동 시작 폴더의 모든 프로그램 실행:

`dex --autostart`

- 지정된 폴더의 모든 프로그램 실행:

`dex --autostart --search-paths {{경로/대상/폴더1}}:{{경로/대상/폴더2}}:{{경로/대상/폴더3}}:`

- GNOME 특정 자동 시작에서 실행될 프로그램 미리보기:

`dex --autostart --environment {{GNOME}}`

- 일반 자동 시작에서 실행될 프로그램 미리보기:

`dex --autostart --dry-run`

- DesktopEntry 속성 `Name`의 값 미리보기:

`dex --property {{Name}} {{경로/대상/파일.desktop}}`

- 현재 디렉토리에서 프로그램에 대한 DesktopEntry 생성:

`dex --create {{경로/대상/파일.desktop}}`

- 주어진 터미널에서 단일 프로그램 실행 (`Terminal=true`가 데스크탑 파일에 있는 경우):

`dex --term {{터미널}} {{경로/대상/파일.desktop}}`
