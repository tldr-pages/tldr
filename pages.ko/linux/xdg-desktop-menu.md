# xdg-desktop-menu

> 데스크탑 메뉴 항목을 설치하거나 제거하는 명령줄 도구.
> 더 많은 정보: <https://manned.org/xdg-desktop-menu>.

- 애플리케이션을 데스크탑 메뉴 시스템에 설치:

`xdg-desktop-menu install {{경로/대상/파일.desktop}}`

- 벤더 접두사 확인을 비활성화하고 애플리케이션을 데스크탑 메뉴 시스템에 설치:

`xdg-desktop-menu install --novendor {{경로/대상/파일.desktop}}`

- 애플리케이션을 데스크탑 메뉴 시스템에서 제거:

`xdg-desktop-menu uninstall {{경로/대상/파일.desktop}}`

- 데스크탑 메뉴 시스템 강제 업데이트:

`xdg-desktop-menu forceupdate --mode {{user|system}}`
