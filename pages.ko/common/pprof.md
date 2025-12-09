# pprof

> 프로파일 데이터의 시각화 및 분석을 위한 명령줄 도구.
> 더 많은 정보: <https://github.com/google/pprof>.

- 특정 프로파일링 파일에서 텍스트 보고서 생성, fibbo 바이너리에 대해:

`pprof -top {{./fibbo}} {{./fibbo-프로필.pb.gz}}`

- 그래프를 생성하고 웹 브라우저에서 열기:

`pprof -svg {{./fibbo}} {{./fibbo-프로필.pb.gz}}`

- 대화형 모드에서 pprof 실행하여 파일에 수동으로 `pprof` 실행 가능:

`pprof {{./fibbo}} {{./fibbo-프로필.pb.gz}}`

- `pprof` 위에 웹 인터페이스를 제공하는 웹 서버 실행:

`pprof -http={{localhost:8080}} {{./fibbo}} {{./fibbo-프로필.pb.gz}}`

- HTTP 서버에서 프로파일을 가져와 보고서 생성:

`pprof {{http://localhost:8080/debug/pprof}}`
