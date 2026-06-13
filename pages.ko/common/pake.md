# pake

> Rust/Tauri를 사용하여 웹페이지를 데스크탑 앱으로 변환.
> 더 많은 정보: <https://github.com/tw93/Pake>.

- 웹페이지 패키징:

`pake {{https://www.google.com/}}`

- 특정 창 크기로 웹페이지 패키징:

`pake --width {{800}} --height {{600}} {{https://www.google.com/}}`

- 사용자 지정 애플리케이션 이름과 아이콘으로 웹페이지 패키징:

`pake --name {{Google}} --icon {{경로/대상/icon.ico}} {{https://www.google.com/}}`

- 크기 조정이 불가능한 창으로 웹페이지 패키징:

`pake --no-resizable {{https://www.google.com/}}`

- 전체 화면 모드로 웹페이지 패키징:

`pake --fullscreen {{https://www.google.com/}}`

- 투명한 타이틀 바로 웹페이지 패키징:

`pake --transparent {{https://www.google.com/}}`
