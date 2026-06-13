# pamfunc

> Netpbm 이미지에 간단한 산술 함수를 적용.
> 더 많은 정보: <https://netpbm.sourceforge.net/doc/pamfunc.html>.

- 지정된 PAM 이미지의 각 샘플에 `n`을 두 번째 인수로 하여 지정된 산술 함수 적용:

`pamfunc -{{multiplier|divisor|adder|subtractor|min|max}} {{n}} {{경로/대상/입력.pam}} > {{경로/대상/출력.pam}}`

- 지정된 PAM 이미지의 각 샘플에 `n`을 두 번째 인수로 하여 지정된 비트 문자열 함수 적용:

`pamfunc -{{andmask|ormask|xormask|shiftleft|shiftright}} {{n}} {{경로/대상/입력.pam}} > {{경로/대상/출력.pam}}`
