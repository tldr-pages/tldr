# stressapptest

> 사용자 영역 메모리 및 IO 테스트.
> 더 많은 정보: <https://github.com/stressapptest/stressapptest>.

- 주어진 메모리 용량(메가바이트 단위)을 테스트:

`stressapptest -M {{메모리}}`

- 메모리와 지정된 파일의 I/O를 테스트:

`stressapptest -M {{메모리}} -f {{경로/대상/파일}}`

- 상세 수준을 지정하여 테스트 (0=최저, 20=최고, 8=기본):

`stressapptest -M {{메모리}} -v {{수준}}`
