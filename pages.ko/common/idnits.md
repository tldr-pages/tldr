# idnits

> 제출 니트에 대한 인터넷 초안을 확인.
> <https://www.ietf.org/id-info/checklist>에 나열된 요구 사항의 섹션 2.1 및 2.2에 대한 위반 사항을 찾음.
> 더 많은 정보: <https://github.com/ietf-tools/idnits>.

- 파일에서 니트를 확인:

`idnits {{경로/대상/파일.txt}}`

- 표시하지 않고 니트 수 계산:

`idnits --nitcount {{경로/대상/파일.txt}}`

- 위반 라인에 대한 추가 정보 표시:

`idnits --verbose {{경로/대상/파일.txt}}`

- 현재 연도 대신 상용구에 지정된 연도를 예상:

`idnits --year {{2021}} {{경로/대상/파일.txt}}`

- 문서가 지정된 상태에 있다고 가정:

`idnits --doctype {{standard|informational|experimental|bcp|ps|ds}} {{경로/대상/파일.txt}}`
