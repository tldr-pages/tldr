# devpod

> 도커, 쿠버네티스, SSH를 사용해서 재현 가능한 개발 환경을 시작.
> 더 많은 정보: <https://devpod.sh/docs/quickstart/devpod-cli/>.

- 도커 또는 쿠버네티스에 프로바이더 추가:

`devpod provider add {{프로바이더_이름}}`

- 사용 가능한 모든 프로바이더 나열:

`devpod provider list-available`

- 특정 IDE를 사용해 GitHub 저장소에서 작업공간을 시작:

`devpod up {{github.com/사용자/레포지토리}} {{[-i|--ide]}} {{vscode}}`

- 로컬 디렉터리에서 작업공간 시작:

`devpod up {{경로/대상/프로젝트}}`

- 존재하는 작업공간을 다시 생성:

`devpod up {{작업공간_이름}} {{[-r|--recreate]}}`

- 작업공간을 초기 상태로 재설정:

`devpod up {{작업공간_이름}} {{[-x|--reset]}}`

- GitHub 레포지토리에 사용자 지정 프로바이더 추가:

`devpod provider add {{조직/프로바이더-레포지토리}}`
