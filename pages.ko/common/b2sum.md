# b2sum

> BLACK2 암호화 체크섬을 계산하십시오.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/b2sum>.

- 파일의 BLACKE2 체크섬 계산:

`b2sum {{filename1}}`

- 여러 파일의 BLACKE2 체크섬 계산:

`b2sum {{filename1}} {{filename2}}`

- BLAKE2 합계 파일 및 파일 이름을 읽고 모든 파일에 일치하는 체크섬이 있는지 확인:

`b2sum -c {{filename.b2}}`

- `stdin`에서 BLACK2 체크섬 계산:

`{{somecommand}} | b2sum`
