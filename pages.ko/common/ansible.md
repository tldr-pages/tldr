# ansible

> SSH를 통해 컴퓨터 그룹을 원격으로 관리. (`/etc/ansible/hosts` 파일을 사용하여 새 그룹/호스트를 추가하십시오).
> `galaxy`와 같은 일부 하위 명령에는 자체 사용 설명서가 있음.
> 더 많은 정보: <https://docs.ansible.com/ansible/latest/cli/ansible.html>.

- 그룹에 속한 호스트 목록:

`ansible {{그룹명}} --list-hosts`

- 핑 모듈을 호출하여 호스트 그룹 핑:

`ansible {{그룹명}} {{[-m|--module-name]}} ping`

- 설정 모듈을 호출하여 호스트 그룹에 대한 사실 표시:

`ansible {{그룹명}} {{[-m|--module-name]}} setup`

- 명령 모듈을 인수로 호출하여 호스트 그룹에서 명령어 실행:

`ansible {{그룹명}} {{[-m|--module-name]}} command {{[-a|--args]}} '{{나의_명령어}}'`

- 관리자 권한으로 명령어 실행:

`ansible {{그룹명}} {{[-b|--become]}} --ask-become-pass {{[-m|--module-name]}} command {{[-a|--args]}} '{{나의_명령어}}'`

- 사용자 정의 인벤토리 파일을 사용하여 명령어 실행:

`ansible {{그룹}} {{[-i|--inventory]}} {{인벤토리_파일}} {{[-m|--module-name]}} command {{[-a|--args]}} '{{나의_명령어}}'`

- 인벤토리의 그룹을 나열:

`ansible localhost {{[-m|--module-name]}} debug {{[-a|--args]}} '{{var=groups.keys()}}'`
