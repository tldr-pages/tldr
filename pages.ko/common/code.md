# code

> 확장 가능한 크로스 플랫폼 코드 에디터.
> 더 많은 정보: <https://github.com/microsoft/vscode>.

- Visual Studio Code 실행:

`code`

- 특정 파일 혹은 디렉토리 열기

`code {{파일/혹은/디렉토리의/경로1 파일/혹은/디렉토리의/경로2 ...}}`

- 두 파일 비교

`code --diff {{파일의/경로1}} {{파일의/경로2}}`

- 특정 파일 혹은 디렉토리를 새로운 창에서 열기

`code --new-window {{파일/혹은/디렉토리의/경로1 파일/혹은/디렉토리의/경로2 ...}}`

- 특정 확장 프로그램 설치/삭제

`code --{{install|uninstall}}-extension {{publisher.extension}}`

- 설치된 확장 프로그램 나열

`code --list-extensions`

- 설치된 확장 프로그램을 버전과 함께 나열

`code --list-extensions --show-versions`

- 사용자 정보를 특정 디렉토리에 저장하면서 관리자 (루트) 권한으로 에디터 실행

`sudo code --user-data-dir {{디렉토리/경로}}`
