# osv-scanner

> 다양한 매체에서 의존성을 스캔하고 OSV 데이터베이스와 대조합니다.
> 더 많은 정보: <https://osv.dev/about>.

- Docker 이미지를 스캔:

`osv-scanner -D {{도커_이미지_이름}}`

- 패키지 잠금 파일을 스캔:

`osv-scanner -L {{경로/대상/잠금파일}}`

- SBOM 파일을 스캔:

`osv-scanner -S {{경로/대상/sbom_파일}}`

- 여러 디렉토리를 재귀적으로 스캔:

`osv-scanner -r {{디렉토리1 디렉토리2 ...}}`

- Git 저장소 스캔 건너뛰기:

`osv-scanner --skip-git {{-r|-D}} {{대상}}`

- 결과를 JSON 형식으로 출력:

`osv-scanner --json {{-D|-L|-S|-r}} {{대상}}`
