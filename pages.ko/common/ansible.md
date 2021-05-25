# ansible

> SSH를 통해 컴퓨터 그룹을 원격으로 관리.
> `/etc/ansible/hosts` 파일을 사용하여 새 그룹/호스트를 추가하십시오.
> 더 많은 정보: <https://www.ansible.com/>.

- 그룹에 속한 호스트 목록:

`ansible {{그룹명}} --list-hosts`

- 핑 모듈을 호출하여 호스트 그룹 핑:

`ansible {{그룹명}} -m ping`

- 설정 모듈을 호출하여 호스트 그룹에 대한 사실 표시:

`ansible {{그룹명}} -m setup`

- 명령 모듈을 인수로 호출하여 호스트 그룹에서 명령어 실행:

`ansible {{그룹명}} -m command -a '{{나의_명령어}}'`

- 관리자 권한으로 명령어 실행:

`ansible {{그룹명}} --become --ask-become-pass -m command -a '{{나의_명령어}}'`

- 사용자 정의 인벤토리 파일을 사용하여 명령어 실행:

`ansible {{그룹}} -i {{인벤토리_파일}} -m command -a '{{나의_명령어}}'`
