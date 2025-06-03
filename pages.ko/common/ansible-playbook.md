# ansible-playbook

> SSH를 통해 원격 머신에서 playbook에 정의된 작업 실행.
> 더 많은 정보: <https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html>.

- playbook에서 작업 실행:

`ansible-playbook {{playbook}}`

- 사용자 정의 호스트 인벤토리를 포함한 playbook에서 작업 실행:

`ansible-playbook {{playbook}} {{[-i|--inventory]}} {{인벤토리_파일}}`

- 명령어로 정의된 추가 변수를 사용하여 playbook에서 작업 실행:

`ansible-playbook {{playbook}} {{[-e|--extra-vars]}} "{{변수1}}={{값1}} {{변수2}}={{값2}}"`

- json 파일에 정의된 추가 변수를 사용하여 playbook에서 작업 실행:

`ansible-playbook {{playbook}} {{[-e|--extra-vars]}} "@{{변수.json}}"`

- 지정된 태그에 대해 플레이북에서 작업 실행:

`ansible-playbook {{playbook}} {{[-t|--tags|]}} {{태그1,태그2}}`

- 특정 작업에서 시작하는 playbook에서 작업 실행:

`ansible-playbook {{playbook}} --start-at {{작업_이름}}`

- 변경사항을 적용하지 않고 플레이북에서 작업 실행(dry-run):

`ansible-playbook {{playbook}} {{[-C|--check|]}} {{[-D|--diff|]}}`
