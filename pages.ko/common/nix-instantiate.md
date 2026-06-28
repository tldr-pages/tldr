# nix-instantiate

> nix 표현식으로부터 store derivation을 생성.
> 관련 항목: `nix eval`.
> 더 많은 정보: <https://nix.dev/manual/nix/latest/command-ref/nix-instantiate.html>.

- Nix 파일에서 store derivation을 생성:

`nix-instantiate {{경로/대상/파일.nix}}`

- 표현식 평가:

`nix-instantiate --eval {{[-E|--expr]}} {{표현식}}`

- 기계가 읽을 수 있는 형식으로 표현식 평가:

`nix-instantiate --eval --xml {{[-E|--expr]}} {{표현식}}`

- 원시(Raw) 출력으로 표현식을 평가(함수의 반환 값은 문자열이어야 함):

`nix-instantiate --eval --raw {{[-E|--expr]}} {{표현식}}`

- 지정한 파일의 Nix 표현식 평가:

`nix-instantiate --eval {{경로/대상/파일.nix}}`
