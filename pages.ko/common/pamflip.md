# pamflip

> PAM 또는 PNM 이미지를 뒤집거나 회전.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pamflip.html>.

- 입력 이미지를 특정 각도로 반시계 방향으로 회전:

`pamflip {{[-r|-rotate]}}{{90|180|270}} {{경로/대상/입력.pam}} > {{경로/대상/출력.pam}}`

- 왼쪽과 오른쪽을 뒤집기:

`pamflip {{[-lr|-leftright]}} {{경로/대상/입력.pam}} > {{경로/대상/출력.pam}}`

- 위쪽과 아래쪽을 뒤집기:

`pamflip {{[-tb|-topbottom]}} {{경로/대상/입력.pam}} > {{경로/대상/출력.pam}}`

- 입력 이미지를 주 대각선으로 뒤집기:

`pamflip {{[-xy|-transpose]}} {{경로/대상/입력.pam}} > {{경로/대상/출력.pam}}`
