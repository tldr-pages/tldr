# repren

> 다중 패턴 문자열 교체 및 파일 이름 바꾸기 도구.
> 더 많은 정보: <https://github.com/jlevy/repren>.

- PNG 파일이 있는 디렉토리에서 리터럴 문자열 교체로 이름을 바꾸는 예비 실행:

`repren --dry-run --rename --literal --from '{{찾을_문자열}}' --to '{{교체할_문자열}}' {{*.png}}`

- JPEG 파일이 있는 디렉토리에서 정규 표현식을 사용하여 이름을 바꾸는 예비 실행:

`repren --rename --dry-run --from '{{정규_표현식}}' --to '{{교체할_문자열}}' {{*.jpg}} {{*.jpeg}}`

- CSV 파일이 있는 디렉토리의 내용에서 찾기 및 교체 실행:

`repren --from '{{([0-9]+) 예제_문자열}}' --to '{{교체할_문자열 \1}}' {{*.csv}}`

- 패턴 파일을 사용하여 찾기 및 교체와 이름 바꾸기 작업을 동시에 실행:

`repren --patterns {{경로/대상/패턴_파일.ext}} --full {{*.txt}}`

- 대소문자를 구분하지 않고 이름 바꾸기:

`repren --rename --insensitive --patterns {{경로/대상/패턴_파일.ext}} *`
