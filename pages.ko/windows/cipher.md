# cipher

> NTFS 볼륨에서 디렉터리와 파일의 암호화를 표시하거나 변경.
> 더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/cipher>.

- 특정 암호화된 파일 또는 디렉터리에 대한 정보 표시:

`cipher /c:{{경로\대상\파일_또는_디렉터리}}`

- 파일 또는 디렉터리를 [e]암호화 (디렉터리가 표시되므로 이후에 추가된 파일도 암호화됨):

`cipher /e:{{경로\대상\파일_또는_디렉터리}}`

- 파일 또는 디렉터리 [d]암호 해독:

`cipher /d:{{경로\대상\파일_또는_디렉터리}}`

- 파일 또는 디렉터리를 안전하게 제거:

`cipher /w:{{경로\대상\파일_또는_디렉터리}}`
