# onefetch

> 로컬 Git 저장소에 대한 프로젝트 정보 및 코드 통계를 표시.
> 더 많은 정보: <https://github.com/o2sh/onefetch/wiki/command-line-options>.

- 현재 작업 디렉토리의 Git 저장소에 대한 통계 표시:

`onefetch`

- 지정된 디렉토리의 Git 저장소에 대한 통계 표시:

`onefetch {{경로/대상/폴더}}`

- 봇에 의해 만들어진 커밋 무시:

`onefetch --no-bots`

- 병합 커밋 무시:

`onefetch --no-merges`

- 언어 로고의 ASCII 아트를 출력하지 않음:

`onefetch --no-art`

- `n`명의 작성자, 언어 또는 파일 변경량을 표시 (기본값: 각각 3, 6, 3):

`onefetch --number-of-{{authors|languages|file-churns}} {{n}}`

- 지정된 파일 및 디렉토리 무시:

`onefetch {{[-e|--exclude]}} {{경로/대상/파일_또는_폴더|정규식}}`

- 지정된 범주에서만 언어 감지 (기본값: 프로그래밍 및 마크업):

`onefetch {{[-T|--type]}} {{programming|markup|prose|data}}`
