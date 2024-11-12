# apkleaks

> APK 파일에서 URI, 엔드포인트, 비밀을 노출.
> 참고: APKLeaks는 `jadx` 디스어셈블러를 사용하여 APK 파일을 디컴파일.
> 더 많은 정보: <https://github.com/dwisiswant0/apkleaks>.

- APK 파일([f]ile)에서 URI, 엔드포인트, 비밀을 스캔:

`apkleaks --file {{경로/대상/파일.apk}}`

- 출력([o]utput)을 스캔하여 특정 파일에 저장:

`apkleaks --file {{경로/대상/파일.apk}} --output {{경로/대상/출력파일.txt}}`

- `jadx` 디스어셈블러 인수([a]rguments) 전달:

`apkleaks --file {{경로/대상/파일.apk}} --args "{{--threads-count 5 --deobf}}"`
