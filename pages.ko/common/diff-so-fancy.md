# diff-so-fancy

> `diff` 출력 결과를 사람이 읽기 쉽게 색상으로 강조.
> 더 많은 정보: <https://github.com/so-fancy/diff-so-fancy#-usage>.

- `diff` 결과를 색상으로 표시:

`diff {{[-u|--unified]}} {{경로/대상/파일1}} {{경로/대상/파일2}} | diff-so-fancy`

- Git 인터랙티브 스테이징 과정에서 `diff-so-fancy`로 출력이 색상화되도록 설정:

`git config --global interactive.diffFilter "diff-so-fancy --patch"`
