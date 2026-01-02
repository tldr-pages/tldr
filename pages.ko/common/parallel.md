# parallel

> 여러 CPU 코어에서 명령 실행.
> 더 많은 정보: <https://www.gnu.org/software/parallel/man.html>.

- 모든 코어를 사용하여 여러 파일을 동시에 gzip 압축:

`parallel gzip ::: {{경로/대상/파일1 경로/대상/파일2 ...}}`

- `stdin`에서 인수를 읽어, 동시에 4개의 작업 실행:

`ls *.txt | parallel -j4 gzip`

- JPEG 이미지를 PNG로 변환, 치환 문자열 사용:

`parallel convert {} {.}.png ::: *.jpg`

- 평행 xargs, 가능한 많은 인수를 하나의 명령에 cram:

`{{인수들}} | parallel -X {{명령어}}`

- `stdin`을 약 1M 블록으로 나누고, 각 블록을 새 명령의 `stdin`으로 전달:

`cat {{큰_파일.txt}} | parallel --pipe --block 1M {{명령어}}`

- SSH를 통해 여러 머신에서 실행:

`parallel -S {{머신1}},{{머신2}} {{명령어}} ::: {{인수1}} {{인수2}}`

- 텍스트 파일에 있는 링크로부터 4개의 파일을 동시에 다운로드, 진행 상황 표시:

`parallel -j4 --bar --eta wget -q {} :::: {{경로/대상/링크.txt}}`

- `parallel`이 실행 중인 작업을 `stderr`에 출력:

`parallel -t {{명령어}} ::: {{인수들}}`
