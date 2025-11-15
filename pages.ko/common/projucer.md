# Projucer

> JUCE 프레임워크 애플리케이션을 위한 프로젝트 관리자.
> 더 많은 정보: <https://docs.juce.com/master/projucer_manual.html#projucer_manual_tools_command_line_tools>.

- 프로젝트에 대한 정보 표시:

`Projucer --status {{경로/대상/프로젝트_파일}}`

- 프로젝트의 모든 파일 및 리소스 다시 저장:

`Projucer --resave {{경로/대상/프로젝트_파일}}`

- 프로젝트의 버전 번호 업데이트:

`Projucer --set-version {{버전_번호}} {{경로/대상/프로젝트_파일}}`

- PIP 파일에서 JUCE 프로젝트 생성:

`Projucer --create-project-from-pip {{경로/대상/PIP}} {{경로/대상/출력}}`

- 모든 JUCE 스타일 주석 (`//=====`, `//-----` 또는 `///////`) 제거:

`Projucer --tidy-divider-comments {{경로/대상/대상_폴더}}`

- 도움말 표시:

`Projucer --help`
