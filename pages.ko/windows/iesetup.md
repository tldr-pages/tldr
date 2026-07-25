# iesetup

> 사용자 지정 Internet Explorer Wizard (`iewzd`) 설치 프로그램을 생성.
> Internet Explorer Administration Kit (IEAK)의 일부.
> 참고: 사용하는 IEAK 버전에 따라 `iesetup` 대신 `Ie11setup`(IE 11)과 같은 실행 파일을 사용.
> 더 많은 정보: <https://learn.microsoft.com/previous-versions/windows/internet-explorer/ie-it-pro/internet-explorer-11/ie11-ieak/iexpress-command-line-options>.

- `iewzd` 문서 보기:

`tldr {{[-p|--platform]}} windows iewzd`

- `iewzd` 실행 파일 위치 지정해, 사용자 지정 Internet Explorer Wizard 실행 파일 생성:

`iesetup /c:"{{경로\대상\iewzd.exe}}"`

- 사용자 지정 설치 프로그램에 `iewzd` 프로그램 인수 적용:

`iesetup /c:"{{경로\대상\iewzd.exe}} {{iewzd_args}}"`

- 관리자([a]dministrator) 또는 일반 사용자([u]ser) 권한을 가정해, 조용한([q]uiet) 모드로 빌드 실행:

`iesetup /q:{{a|u}} /c:"{{경로\대상\iewzd.exe}} {{iewzd_args}}"`

- 설치 완료 후 다시 시작([r]estart) 동작 설정 ([a]sk: 확인, [n]ever: 안 함, alway[s]: 항상):

`iesetup /r:{{a|n|s}} /c:"{{경로\대상\iewzd.exe}} {{iewzd_args}}"`
