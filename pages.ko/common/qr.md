# qr

> ANSI VT-100 이스케이프 코드를 사용하여 터미널에서 QR 코드를 생성.
> 더 많은 정보: <https://manned.org/qr>.

- QR 코드 생성:

`echo "{{데이터}}" | qr`

- 오류 수정 수준 지정 (기본값은 M):

`echo "{{데이터}}" | qr --error-correction={{L|M|Q|H}}`
