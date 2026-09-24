# dosbox

> 레거시 DOS 애플리케이션과 게임을 실행하기 위한 MS-DOS 에뮬레이터.
> 더 많은 정보: <https://www.dosbox.com/wiki/Usage>.

- 기본 설정으로 DOSBox 실행:

`dosbox`

- 특정 경로의 DOS 실행 파일 실행:

`dosbox {{경로/대상/실행파일.exe}}`

- 폴더를 C: 드라이브로 마운트하고 실행파일 실행:

`dosbox {{경로/대상/실행파일.exe}} -c "MOUNT C {{경로/대상/폴더}}"`

- 전체 화면 모드로 DOSBox 실행:

`dosbox -fullscreen`

- DOSBox 실행 후 자동 종료:

`dosbox {{경로/대상/실행파일.exe}} -exit`
