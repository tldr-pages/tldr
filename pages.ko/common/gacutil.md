# gacutil

> 전역 어셈블리 캐시 (Global Assembly Cache, CAG) 관리 유틸리티.
> 더 많은 정보: <https://manned.org/gacutil>.

- 지정된 어셈블리를 GAC에 설치:

`gacutil -i {{경로/대상/어셈블리.dll}}`

- GAC에서 지정된 어셈블리를 제거:

`gacutil -i {{어셈블리_표시_이름}}`

- GAC의 내용을 출력:

`gacutil -l`
