# readarray

> `stdin`에서 여러 줄을 읽어 배열에 저장.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-readarray>.

- 대화형으로 여러 줄을 입력받아 배열에 저장:

`readarray {{배열_이름}}`

- 파일의 각 줄을 읽어 배열에 저장:

`readarray < {{경로/대상/파일.txt}} {{배열_이름}}`

- 각 줄 끝([t]railing)의 구분자 (기본값: 줄바꿈 문자) 제거:

`readarray < {{경로/대상/파일.txt}} -t {{배열_이름}}`

- 최대 `n`줄까지만 읽어 배열에 저장:

`readarray < {{경로/대상/파일.txt}} -n {{n}} {{배열_이름}}`

- `n`줄을 건너뛰고([s]kip) 배열에 저장:

`readarray < {{경로/대상/파일.txt}} -s {{n}} {{배열_이름}}`

- 사용자 지정 구분자([d]elimiter) 지정:

`readarray < {{경로/대상/파일.txt}} -d {{구분자}} {{배열_이름}}`

- 도움말 표시:

`help mapfile`
