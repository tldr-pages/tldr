# pw-profiler

> 로컬 또는 원격 인스턴스를 프로파일링.
> 더 많은 정보: <https://docs.pipewire.org/page_man_pw-profiler_1.html>.

- 기본 인스턴스를 프로파일링하고 `profile.log`에 기록 (`gnuplot` 파일과 결과 시각화를 위한 HTML 파일도 생성됨):

`pw-profiler`

- 로그 출력 파일 변경:

`pw-profiler --output {{경로/대상/파일.log}}`

- 원격 인스턴스를 프로파일링:

`pw-profiler --remote {{원격_이름}}`

- 도움말 표시:

`pw-profiler --help`
