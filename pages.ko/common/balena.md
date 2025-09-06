# balena

> 명령 줄에서 balenaCloud, openBalena 및 balena API와 상호 작용하십시오.
> 더 많은 정보: <https://www.balena.io/docs/reference/cli/>.

- balenaCloud 계정에 로그인:

`balena login`

- BalencaCloud 또는 OpenBalena 애플리케이션 생성:

`balena app create {{app_name}}`

- 계정 내 모든 balenaCloud 또는 openBalena 애플리케이션 나열:

`balena apps`

- balenaCloud 또는 openBalena 계정과 관련된 모든 장치 나열:

`balena devices`

- BalenaOS 이미지를 로컬 드라이브에 플래시:

`balena local flash {{path/to/balenaos.img}} --drive {{drive_location}}`
