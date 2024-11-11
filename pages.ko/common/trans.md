# trans

> Translate Shell은 명령줄 번역기입니다.
> 더 많은 정보: <https://github.com/soimort/translate-shell>.

- 단어 번역 (언어는 자동으로 감지됨):

`trans "{{번역할_단어나_문장}}"`

- 간단한 번역 받기:

`trans --brief "{{번역할_단어나_문장}}"`

- 단어를 프랑스어로 번역:

`trans :{{fr}} {{단어}}`

- 독일어에서 영어로 단어 번역:

`trans {{de}}:{{en}} {{Schmetterling}}`

- 사전처럼 행동하여 단어의 의미 얻기:

`trans -d {{단어}}`
