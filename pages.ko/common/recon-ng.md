# recon-ng

> 자동화된 정찰 및 정보 수집 도구.
> 더 많은 정보: <https://github.com/lanmaster53/recon-ng/wiki>.

- 대화형 모드로 도구 실행:

`recon-ng`

- [대화형] 작업 공간 생성:

`workspaces create {{워크스페이스_이름}}`

- [대화형] 다양한 정찰 작업에 사용할 모듈을 marketplace에서 검색:

`marketplace search`

- [대화형] 사용 가능한 모든 모듈 설치 (일부 모듈은 완전한 기능 동작을 위해 API 키가 필요할 수 있음):

`marketplace install all`

- [대화형] profiler 모듈 로드, 대상과 일치하는 웹 프로필을 검색 및 수집하여 저장:

`modules load profiler`

- [대화형] 대상의 사용자명 입력. 명령 실행 후, 검색할 사용자 이름을 입력하고 나머지 옵션은 비워둠:

`db insert profiles`

- [대화형] 현재 모듈 실행:

`run`
