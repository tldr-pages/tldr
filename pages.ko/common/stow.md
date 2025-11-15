# stow

> 심볼릭 링크 관리자.
> 주로 dotfiles 관리를 위해 사용됩니다.
> 같이 보기: `chezmoi`, `tuckr`, `vcsh`, `homeshick`.
> 더 많은 정보: <https://www.gnu.org/software/stow/manual/stow.html#Invoking-Stow>.

- 모든 파일을 주어진 디렉토리에 재귀적으로 심볼릭 링크 생성:

`stow --target={{경로/대상/디렉토리}} {{파일1 디렉토리1 파일2 디렉토리2}}`

- 주어진 디렉토리에서 심볼릭 링크를 재귀적으로 삭제:

`stow --delete --target={{경로/대상/디렉토리}} {{파일1 디렉토리1 파일2 디렉토리2}}`

- 결과가 어떻게 될지 시뮬레이션:

`stow --simulate --target={{경로/대상/디렉토리}} {{파일1 디렉토리1 파일2 디렉토리2}}`

- 삭제 후 다시 심볼릭 링크 생성:

`stow --restow --target={{경로/대상/디렉토리}} {{파일1 디렉토리1 파일2 디렉토리2}}`

- 정규 표현식과 일치하는 파일 제외:

`stow --ignore={{정규_표현식}} --target={{경로/대상/디렉토리}} {{파일1 디렉토리1 파일2 디렉토리2}}`
