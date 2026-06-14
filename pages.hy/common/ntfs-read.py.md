# ntfs-read.py

> Միայն կարդալու NTFS հետազոտող՝ NTFS հատորներից ֆայլեր մուտք գործելու և հանելու համար:.
> Impacket փաթեթի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/fortra/impacket>:.

- Բացեք NTFS ծավալը հետազոտության համար (օրինակ՝ `C:\.\\` կամ `/dev/disk1s1`):

`ntfs-read.py {{volume}}`

- Արտահանեք որոշակի ֆայլ NTFS ծավալից (օրինակ՝ `\windows\system32\config\sam`):

`ntfs-read.py -extract {{\windows\system32\config\sam}} {{volume}}`

- Միացնել վրիպազերծման ելքը.:

`ntfs-read.py -debug {{volume}}`

- Ցուցադրել օգնությունը.:

`ntfs-read.py --help`
