# qrencode

> QR 코드 생성기. PNG와 EPS를 지원합니다.
> 더 많은 정보: <https://manned.org/qrencode>.

- 문자열을 QR 코드로 변환하여 출력 파일로 저장:

`qrencode -o {{경로/대상/출력_파일.png}} {{문자열}}`

- 입력 파일을 QR 코드로 변환하여 출력 파일로 저장:

`qrencode -o {{경로/대상/출력_파일.png}} -r {{경로/대상/입력_파일}}`

- 문자열을 QR 코드로 변환하여 터미널에 출력:

`qrencode -t ansiutf8 {{문자열}}`

- 파이프로부터 입력을 받아 QR 코드로 변환하여 터미널에 출력:

`echo {{문자열}} | qrencode -t ansiutf8`
