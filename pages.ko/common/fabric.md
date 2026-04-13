# fabric

> AI를 활용해 인간의 작업을 확장하는 오픈소스 프레임워크.
> 크라우드 소싱된 AI 프롬프트 집합을 활용하여 특정 문제를 해결하는 모듈형 구조를 제공.
> 더 많은 정보: <https://github.com/danielmiessler/fabric#usage>.

- fabric 설정 실행:

`fabric {{[-S|--setup]}}`

- 사용 가능한 모든 패턴 목록 조회:

`fabric {{[-l|--listpatterns]}}`

- 파일 입력을 사용하여 패턴 실행:

`fabric < {{경로/대상/입력_파일}} {{[-p|--pattern]}} {{패턴_이름}}`

- YouTube 영상 URL을 대상으로 패턴 실행:

`fabric {{[-y|--youtube]}} "{{https://www.youtube.com/watch?v=video_id}}" {{[-p|--pattern]}} {{패턴_이름}}`

- 여러 패턴을 파이프로 연결해 실행:

`fabric {{[-p|--pattern]}} {{패턴1}} | fabric {{[-p|--pattern]}} {{패턴2}}`

- 사용자 정의 패턴 실행:

`fabric {{[-p|--pattern]}} {{사용자정의_패턴_이름}}`

- 패턴 실행 결과를 파일로 저장:

`fabric {{[-p|--pattern]}} {{패턴_이름}} {{[-o|--output]}} {{경로/대상/출력_파일}}`

- 변수 값을 지정하여 패턴 실행:

`fabric {{[-p|--pattern]}} {{패턴_이름}} {{[-v|--variable]}} "{{변수_이름}}:{{값}}"`
