# atoum

> PHP를 위한 단순하고 현대적이며 직관적인 단위 테스트 프레임워크.
> 더 많은 정보: <https://atoum.readthedocs.io/en/latest/option_cli.html>.

- 설정 파일 초기화:

`atoum --init`

- 모든 테스트 실행:

`atoum`

- 특정 설정 파일을 사용한 테스트 실행:

`atoum {{[-c|--configuration]}} {{경로/파일명}}`

- 특정 테스트파일 실행:

`atoum {{[-f|--files]}} {{경로/파일명}}`

- 특정 테스트 디렉토리 실행:

`atoum {{[-d|--directories]}} {{경로/디렉토리명}}`

- 특정 namespace 아래 있는 모든 테스트 실행:

`atoum {{[-ns|--namespaces]}} {{namespace}}`

- 특정 태그를 갖고 테스트 실행:

`atoum {{[-t|--tags]}} {{태그}}`

- 테스트를 실행하기 전에 사용자 지정 부트스트랩 파일을 로드:

`atoum {{[-bf|--bootstrap-file]}} {{경로/파일명}}`
