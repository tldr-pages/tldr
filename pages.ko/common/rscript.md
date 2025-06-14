# Rscript

> R 프로그래밍 언어로 스크립트를 실행.
> 더 많은 정보: <https://manned.org/Rscript>.

- 스크립트 실행:

`Rscript {{경로/대상/파일.R}}`

- 바닐라 모드로 스크립트 실행 (세션을 빈 상태로 시작하며 종료 시 작업 공간을 저장하지 않음):

`Rscript --vanilla {{경로/대상/파일.R}}`

- 하나 이상의 R 표현식 실행:

`Rscript -e {{표현식1}} -e {{표현식2}}`

- R 버전 표시:

`Rscript --version`
