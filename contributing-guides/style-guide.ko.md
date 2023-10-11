# 스타일 가이드

이 페이지는 `tldr` 페이지에 대한 형식 지정 지침들을 나열합니다.

## 레이아웃

각 페이지의 기본 포맷은 다음 템플릿과 일치해야 하며, 다음과 최대 8개의 명령어 예제를 포함해야 합니다:

```md
# 명령어 이름

> 짧고 간결한 설명
> 보통 1줄, 필요한 2줄 까지 허용됨
> 더 많은 정보: <https://example.com/command_name/help/page>.

- 코드 설명:

`command_name options`

- 코드 설명:

`command_name options`

...
```

예시:

```md
# 명령어 이름

# krita

> krita는 디지털 아티스트를 위해 설계된 스케치/페인팅 프로그램입니다.
> `gimp` 페이지도 참조하세요.
> 더 많은 정보: <https://docs.krita.org/en/reference_manual/linux_command_line.html>.

- krita 시작:

`krita`

- 로딩 화면 없이 시작:

`krita --nosplash`

- 특정 파일 열기:

`krita {{path/to/image1 path/to/image2 ...}}`

- 특정 workspace (`Animation`) 에서 시작:

`krita --workspace {{Animation}}`

- 전체화면으로 시작:

`krita --fullscreen`
```

> :bulb: 도움말 페이지는 매뉴얼 뿐 아니라 문서, 프로젝트, 튜토리얼 등이 될 수 있습니다.
> 그러나, 문서 페이지를 권장합니다.

위의 형식들을 강제하는 linter가 있습니다.
모든 pull 요청에 대해 자동으로 실행되지만, 제출하기 전 local에서 테스트하기 위해 설치할 수 있습니다.

```sh
npm install --global tldr-lint
tldr-lint path/to/tldr_page.md
```

`tldr-lint`를 사용하기 위한 여러 방법들이 많습니다. 다음은 이에 대한 안내 페이지입니다. 확인해 보세요! [`tldr tldr-lint`](https://github.com/tldr-pages/tldr/blob/main/pages/common/tldr-lint.md).

별칭 `tldrl`을 쓸 수도 있습니다.


Client는 `--render` 명령어를 통해 local에서 페이지를 미리 볼 수 있습니다.

```sh
tldr --render path/to/tldr_page.md
```

### Aliases

만약 명령어를 다른 별칭으로 부를 수 있는 경우 (ex: `vim`과 `vi`) 사용자가 원래 명령 이름을 가리키도록 별칭 페이지를 만들 수 있습니다.

```md
# 명령어 이름

> 이 명령어는 `originam-command-name`의 별칭입니다.
> 더 많은 정보는 <https://example.com/original/command/help/page>를 참조하세요.

- 원래 명령어에 대한 문서:

`tldr vim`

```

- 번역된 별칭 페이지 템플릿은 [여기](https://github.com/tldr-pages/tldr/blob/main/contributing-guides/translation-templates/alias-pages.md)에서 확인할 수 있습니다.

## Token syntax

사용자 입력 값은 `tldr` 클라이언트에게 강조될 수 있도록 `{{token}}` 구문을 사용해야 합니다.

토큰을 선택할 때 다음의 가이드라인을 염두에 두십시오:

### Naming

- 짧지만 설명적인 토큰을 사용하세요.
- 파일 및 디렉토리 경로에 대한 참조의 경우: 
  `{{path/to/<placeholder>}}`의 포맷을 사용하세요.
  (암시적인 경로인 경우는 제외!)
- 경로가 상대경로일 수 없지만 파일 시스템의 root에서 시작해야 하는 경우
  접두사로 `/`를 붙입니다.
  (ex: `get {{/path/to/remote_file
- 파일 및 디렉토리 참조가 모드 가능한 경우
  `{{path/to/file_or_directory}}`를 사용하세요.

### Extensions

- 파일에 특정 확장자가 필요한 경우 추가하십시오.
  (ex: `unrar x {{compressed.rar}}`)
- 만약 일반적인 확장자가 필요하다면, **반드시 필요한 경우에만** `{{.ext}}`를 사용하십시오.
  예시1: `find.md`의 "확장자로 파일 찾기"(`find {{root_path}} -name '{{*.ext}}'`)는 `{{*.ext}}`를 사용하여 불필요한 내용 없이, 구체적이지  않게 설명합니다.
  예시2: `wc -l {{file}}`는 `{{file}}`을 (extension 없이) 사용하는 것 만으로 충분합니다.

### Special Cases

- 만약 명령어가 파일 시스템이나 장치에 돌이킬 수 없는 변경을 수행하는 경우, 모든 예제를 생각 없이 복사하여 붙여넣을 수 없도록 작성하십시오.
  예를 들어 `ddrescue --force --no-scrape /dev/sda /dev/sdb` 대신에 `ddrescue --force --no-scrape {{/dev/sdX}} {{/dev/sdY}}`를 사용하고, *block device*에 `/dev/sda1` 대신 `{{/dev/sdXY}}` 자리 표시자를 사용하세요.
- 명령어가 많은 수의 명령어를 포함할 수 있는 경우, 다음과 같이 생략하여 표현하세요.
  `{{argument1 argument2 ...}}` 여러 옵션 중 하나가 가능한 경우 `{{either|or}}`로 작성합니다.

일반적으로, 토큰은 가능한 한 직관적이어야 합니다.
명령을 사용하는 방법을 파악하고 값으로 채우십시오.

내용 입력란의 기술 문구는 `backtick` 구문을 사용해야 합니다.
다음과 같이 역따옴표를 사용하십시오.

- Paths, ex. `package.json`, `/etc/package.json`.
- Extensions, ex. `.dll`.
- Commands, ex. `ls`.

## Imperative Mood

예시 설명형은 명령법으로 표현되어야 합니다.
예를 들자면 `List all files.`를 `Listing all files`, `File listing` 등 입니다.
이것은 특별한 경우를 제외하고 기본적으로 **모든 번역에 적용**됩니다.

## Serial Comma

3개 이상의 항목 목록을 선언할 때, Oxford 쉼표라고도 부르는 [연속 쉼표](https://en.wikipedia.org/wiki/Serial_comma)를 사용합니다.

> Git brances, tags, remotes를 삭제하세요.

위의 예는 직렬 쉼표를 사용하지 않으므로 다음 두 가지 중 하나를 의미할 수 있습니다.

- `tags`와 `remotes`라는 Git branch들을 삭제하세요.
- Git branches, Git tag, Git remotes를 모두 삭제하세요.

목록의 마지막 요소에서 "and" 또는 "or" 앞에 쉼표를 삽입하면 이 문제를 해결할 수 있습니다.

> Git branches, tags 및 remotes를 삭제하세요.

## More information links

`More information` 줄에는 작성자가 제공한 문서로 연결하는 것을 권장합니다.
사용할 수 없는 경우, 기본 fallback으로 <https://manned.org>를 사용합니다.
