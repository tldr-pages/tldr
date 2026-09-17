# iewzd

> Internet Explorer Setup Wizard: Internet Explorer 설치를 프로그래밍 방식으로 구성.
> 사용자 지정 Internet Explorer 및 `iewzd`를 함께 포함하는 `iesetup`과 혼동하지 말 것.
> 참고: 사용하는 IE 버전에 따라 `iewzd` 대신 `Ie11wzd.exe`, `ie10_setup.exe`, `IE9-Windows6.0-x86-en-us.exe` 등 실행 파일을 사용해야 할 수 있음.
> 더 많은 정보: <https://learn.microsoft.com/previous-versions/windows/internet-explorer/ie-it-pro/internet-explorer-11/ie11-ieak/ie-setup-command-line-options-and-return-codes>.

- `iesetup` 문서 보기:

`tldr {{[-p|--platform]}} windows iesetup`

- Internet Explorer Wizard 실행:

`iewzd`

- Internet Explorer 설치 후 컴퓨터를 강제로 다시 시작하거나 다시 시작하지 않음:

`iewzd {{/norestart|/forcerestart}}`

- Internet Explorer를 기본 브라우저로 설정하지 않음:

`iewzd /no-default`

- Internet Explorer 업데이트 확인 안 함:

`iewzd /update-no`

- 수동 모드(Passive, 진행 상황만 표시) 또는 조용한 모드(Quiet, 화면 표시 없이 백그라운드)로 실행:

`iewzd {{/passive|/quiet}}`

- 설치 로그를 파일에 저장:

`iewzd /log {{경로\대상\파일}}`
