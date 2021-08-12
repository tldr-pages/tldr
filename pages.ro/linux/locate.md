# locate

> Găsiţi rapid numele fişierelor.

- Caută model în baza de date. Notă: baza de date este recomputată periodic (de obicei săptămânal sau zilnic):

`locate {{pattern}}`

- Căutați un fișier după numele exact al fișierului (un model care nu conține caractere globbing este interpretat ca `*patter`):

`locate */{{filename}}`

- Recomate baza de date. Trebuie să o faceți dacă doriți să găsiți fișiere adăugate recent:

`sudo updatedb`
