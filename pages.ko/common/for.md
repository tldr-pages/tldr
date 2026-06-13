# for

> 명령을 여러 번 수행.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#Looping-Constructs>.

- 지정된 각 항목에 대해 지정된 명령을 실행:

`for {{변수}} in {{item1 item2 ...}}; do {{echo "Loop is executed"}}; done`

- 주어진 숫자 범위에 대해 반복:

`for {{변수}} in {{{from}}..{{to}}..{{step}}}; do {{echo "Loop is executed"}}; done`

- 주어진 파일 목록을 반복:

`for {{변수}} in {{경로/대상/파일1 경로/대상/파일2 ...}}; do {{echo "Loop is executed"}}; done`

- 주어진 디렉터리 목록을 반복:

`for {{변수}} in {{경로/대상/디렉터리1/ 경로/대상/디렉터리2/ ...}}; do {{echo "Loop is executed"}}; done`

- 모든 디렉터리에서 주어진 명령을 수행:

`for {{변수}} in */; do (cd "${{변수}}" || continue; {{echo "Loop is executed"}}) done`
