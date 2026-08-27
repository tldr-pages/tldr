# samply

> CPU 프로파일을 샘플링하고 기록하여 분석할 수 있도록 함.
> 더 많은 정보: <https://github.com/mstange/samply>.

- 명령의 프로파일을 기록하고 브라우저에서 열기:

`samply record {{경로/대상/명령어 인자1 인자2 ...}}`

- 샘플링 속도 조정:

`samply record --rate {{샘플링_빈도_Hz}} {{경로/대상/명령어 인자1 인자2 ...}}`

- 브라우저 열기 없이 프로파일을 파일로 저장:

`samply record --save-only --output {{경로/대상/프로파일.json}} -- {{경로/대상/명령어 인자1 인자2 ...}}`

- 이전에 저장한 프로파일을 브라우저에서 열기:

`samply load {{경로/대상/프로파일.json}}`
