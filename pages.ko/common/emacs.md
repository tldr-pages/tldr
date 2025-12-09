# emacs

> 확장 가능, 사용자 정의 가능, 자체 문서화가 되는 실시간 디스플레이 편집기.
> 참고: `emacsclient`.
> 더 많은 정보: <https://www.gnu.org/software/emacs>.

- Emacs 시작 및 파일 열기:

`emacs {{경로/대상/파일}}`

- 지정된 줄 번호에서 파일 열기:

`emacs +{{줄_번호}} {{경로/대상/파일}}`

- Emacs Lisp 파일을 스크립트로 실행:

`emacs --script {{경로/대상/파일.el}}`

- 콘솔 모드에서 Emacs를 시작 (X 윈도우 없이):

`emacs {{[-nw|--no-window-system]}}`

- 백그라운드에서 Emacs 서버를 시작 (`emacsclient`를 통해 액세스 가능):

`emacs --daemon`

- 실행 중인 Emacs 서버와 모든 인스턴스를 중지하고, 저장되지 않은 파일에 대한 확인을 요청:

`emacsclient --eval '(save-buffers-kill-emacs)'`

- Emacs에 파일을 저장:

`<Ctrl x><Ctrl s>`

- Emacs를 종료:

`<Ctrl x><Ctrl c>`
