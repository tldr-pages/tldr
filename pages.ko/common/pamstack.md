# pamstack

> 여러 PAM 이미지의 평면을 하나의 PAM 이미지로 스택.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pamstack.html>.

- 지정된 PAM 이미지의 평면을 특정 순서로 스택:

`pamstack {{경로/대상/이미지1.pam 경로/대상/이미지2.pam ...}} > {{경로/대상/출력.pam}}`

- 출력 PAM 파일의 튜플 타입 이름 지정 (최대 255자):

`pamstack {{[-t|-tupletype]}} {{튜플_타입}} {{경로/대상/이미지1.pam 경로/대상/이미지2.pam ...}} > {{경로/대상/출력.pam}}`
