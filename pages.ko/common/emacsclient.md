# emacsclient

> 기존 Emacs 서버에서 파일을 열기.
> 참고: `emacs`.
> 더 많은 정보: <https://www.gnu.org/software/emacs/manual/html_node/emacs/emacsclient-Options.html>.

- 기존 Emacs 서버에서 파일을 열기 (사용 가능한 경우, GUI 사용):

`emacsclient {{경로/대상/파일}}`

- 콘솔 모드에서 파일 열기 (X 윈도우 없이):

`emacsclient --no-window-system {{경로/대상/파일}}`

- 새로운 Emacs 창에서 파일을 열기:

`emacsclient --create-frame {{경로/대상/파일}}`

- 명령을 평가하고 출력을 `stdout`으로 출력한 다음 종료:

`emacsclient --eval '({{명령어}})'`

- Emacs 서버가 실행되고 있지 않은 경우, 대체 편집기를 지정:

`emacsclient --alternate-editor {{에디터}} {{경로/대상/파일}}`

- 실행 중인 Emacs 서버와 모든 인스턴스를 중지, 저장되지 않은 파일에 대한 확인을 요청:

`emacsclient --eval '(save-buffers-kill-emacs)'`
