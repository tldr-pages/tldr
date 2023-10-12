# ln

> 파일 및 디렉터리에 대한 링크를 생성합니다.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/ln>.

- 파일이나 디렉터리에 대한 심볼릭 링크 생성:

`ln -s {{/path/to/file_or_directory}} {{path/to/symlink}}`

- 다른 파일을 가리키도록 기존 심볼릭 링크를 덮어쓰기:

`ln -sf {{/path/to/new_file}} {{path/to/symlink}}`

- 파일에 대한 하드 링크 생성:

`ln {{/path/to/file}} {{path/to/hardlink}}`
