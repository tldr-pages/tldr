# dexdump

> 안드로이드 DEX 파일들에 대한 정보 출력.
> 더 많은 정보: <https://manned.org/dexdump>.

- APK 파일으로부터 클래스들과 메서드들 추출:

`dexdump {{경로/파일명.apk}}`

- APK 파일에 포함된 DEX 파일들의 헤더 정보 출력:

`dexdump -f {{경로/파일명.apk}}`

- 실행가능한 섹션의 분해된 결과 출력:

`dexdump -d {{경로/파일명.apk}}`

- 파일로 결과 출력:

`dexdump -o {{경로/파일명}} {{경로/파일명.apk}}`
