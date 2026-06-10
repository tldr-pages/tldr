# mp3info

> Դիտող/խմբագիր՝ MP3 ֆայլերի ID3v1 (բայց ոչ ID3v2) պիտակների համար:.
> Լրացուցիչ տեղեկություններ. <https://www.ibiblio.org/mp3info/mp3info.html>:.

- Ցույց տալ կոնկրետ MP3 ֆայլի բոլոր ID3v1 պիտակները.:

`mp3info {{path/to/file.mp3}}`

- Խմբագրել ID3v1 պիտակները [i] interactively:

`mp3info -i {{path/to/file.mp3}}`

- Սահմանեք արժեքներ ID3v1 թեգերի համար կոնկրետ MP3 ֆայլում ([a]rtist, [t]itle, a[l]bum, [y]ear և [c]comment):

`mp3info -a "{{artist_name}}" -t "{{song_title}}" -l "{{album_title}}" -y {{year}} -c "{{comment_text}}" {{path/to/file.mp3}}`

- Սահմանեք ալբոմի երգի [n] թիվը կոնկրետ MP3 ֆայլի համար.:

`mp3info -n {{track_number}} {{path/to/file.mp3}}`

- [G]ստացեք վավեր ժանրերի ցանկ և դրանց թվային կոդերը.:

`mp3info -G`

- Սահմանեք երաժշտությունը [g]enre կոնկրետ MP3 ֆայլի համար.:

`mp3info -g {{genre_number}} {{path/to/file.mp3}}`
