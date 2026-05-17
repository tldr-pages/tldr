# flexget

> 토렌트, nzbs, 팟캐스트, 만화, 시리즈, 영화 등 다양한 콘텐츠를 자동화하는 도구.
> 더 많은 정보: <https://flexget.com/en/CLI>.

- 모든 Flexget 작업을 즉시 실행:

`flexget execute --now`

- Flexget 데몬 시작 및 백그라운드 실행:

`flexget daemon start --daemonize`

- Flexget에 기록된 모든 시리즈 목록 표시:

`flexget series list`

- 설정 파일의 특정 작업 실행:

`flexget -c {{경로/대상/설정파일.yml}} execute --task {{작업_이름}}`
