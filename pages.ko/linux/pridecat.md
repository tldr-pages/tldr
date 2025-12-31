# pridecat

> cat과 유사하지만 더 다채로운 도구 :).
> 더 많은 정보: <https://github.com/lunasorcery/pridecat#flags>.

- 파일의 내용을 프라이드 색상으로 `stdout`에 출력:

`pridecat {{경로/대상/파일}}`

- 파일의 내용을 트랜스 색상으로 출력:

`pridecat {{경로/대상/파일}} --{{transgender|trans}}`

- 레즈비언과 양성애자 프라이드 깃발을 번갈아 사용:

`pridecat {{경로/대상/파일}} --lesbian --bi`

- 파일의 내용을 배경색을 변경하여 출력:

`pridecat {{경로/대상/파일}} -b`

- 디렉터리 내용을 프라이드 깃발 색상으로 나열:

`ls | pridecat --{{flag}}`
