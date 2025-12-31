# scrapy

> 웹 크롤링 프레임워크.
> 더 많은 정보: <https://docs.scrapy.org/en/latest/topics/commands.html#using-the-scrapy-tool>.

- 프로젝트 생성:

`scrapy startproject {{프로젝트_이름}}`

- 스파이더 생성 (프로젝트 디렉토리에서):

`scrapy genspider {{스파이더_이름}} {{웹사이트_도메인}}`

- 스파이더 편집 (프로젝트 디렉토리에서):

`scrapy edit {{스파이더_이름}}`

- 스파이더 실행 (프로젝트 디렉토리에서):

`scrapy crawl {{스파이더_이름}}`

- Scrapy가 인식하는 방식으로 웹페이지를 가져와 `stdout`에 소스 출력:

`scrapy fetch {{URL}}`

- Scrapy가 인식하는 방식으로 웹페이지를 기본 브라우저에서 열기 (더 정확하게 보려면 JavaScript 비활성화):

`scrapy view {{URL}}`

- URL에 대한 Scrapy 셸 열기, 이 셸을 통해 Python 셸(IPython이 가능하다면)을 사용하여 페이지 소스와 상호작용 가능:

`scrapy shell {{URL}}`
