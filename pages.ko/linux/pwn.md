# pwn

> 신속한 프로토타이핑을 위한 Exploit 개발 라이브러리.
> 더 많은 정보: <https://docs.pwntools.com/en/stable/commandline.html>.

- 주어진 어셈블리 코드를 `bytes`로 변환:

`pwn asm "{{xor edi, edi}}"`

- 특정 문자 수의 순환 패턴 생성:

`pwn cyclic {{숫자}}`

- 주어진 데이터를 16진수로 인코딩:

`pwn hex {{deafbeef}}`

- 주어진 데이터를 16진수에서 디코딩:

`pwn unhex {{6c4f7645}}`

- 셸 실행을 위한 x64 Linux 쉘코드 출력:

`pwn shellcraft {{amd64.linux.sh}}`

- 주어진 ELF 파일의 바이너리 보안 설정 확인:

`pwn checksec {{경로/대상/파일}}`

- Pwntools 업데이트 확인:

`pwn update`

- 버전 표시:

`pwn version`
