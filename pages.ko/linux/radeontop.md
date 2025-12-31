# radeontop

> AMD GPU의 사용률을 표시합니다.
> 시스템에 따라 루트 권한이 필요할 수 있습니다.
> 더 많은 정보: <https://github.com/clbr/radeontop/blob/master/radeontop.asc>.

- 기본 AMD GPU의 사용률 표시:

`radeontop`

- 색상 출력 활성화:

`radeontop --color`

- 특정 GPU 선택 (버스 번호는 `lspci` 출력의 첫 번째 숫자입니다):

`radeontop --bus {{버스_번호}}`

- 화면 새로고침 빈도 지정 (값이 클수록 GPU 오버헤드가 증가):

`radeontop --ticks {{초당_샘플_수}}`
