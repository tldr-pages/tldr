# conda doctor

> 환경의 상태 보고서 표시.
> 더 많은 정보: <https://docs.conda.io/projects/conda/en/latest/commands/doctor.html>.

- 현재 활성화된 환경의 보고서 확인:

`conda doctor`

- 이름으로 환경을 지정:

`conda doctor {{[-n|--name]}} {{환경_이름}}`

- 경로로 환경 지정:

`conda doctor {{[-p|--prefix]}} {{경로/대상/환경}}`

- 상세 출력 활성화 (참고: `-v` 플래그를 여러번 사용하면 더욱 상세한 출력 제공):

`conda doctor {{[-v|--verbose]}}`
