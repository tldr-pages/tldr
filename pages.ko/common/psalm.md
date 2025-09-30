# psalm

> PHP 애플리케이션에서 오류를 찾기 위한 정적 분석 도구.
> 더 많은 정보: <https://psalm.dev>.

- Psalm 구성 생성:

`psalm --init`

- 현재 작업 디렉터리 분석:

`psalm`

- 특정 디렉터리나 파일 분석:

`psalm {{경로/대상/파일_또는_폴더}}`

- 특정 구성 파일을 사용하여 프로젝트 분석:

`psalm --config {{경로/대상/psalm.xml}}`

- 출력에 정보성 결과 포함:

`psalm --show-info`

- 프로젝트를 분석하고 통계 표시:

`psalm --stats`

- 4개의 스레드로 병렬 프로젝트 분석:

`psalm --threads {{4}}`
