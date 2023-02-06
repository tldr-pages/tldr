# duti

> Alapértelmezett alkalmazások beállítása dokumentumtípusokhoz és URL-sémákhoz macOS-en. További információ: <https://github.com/moretension/duti>.

- Állítsa be a Safarit a HTML-dokumentumok alapértelmezett kezelőjének:

`duti -s {{com.apple.Safari}} {{public.html}} all`

- Állítsa be a VLC-t a `.m4v` kiterjesztésű fájlok alapértelmezett megjelenítőjének:

`duti -s {{org.videolan.vlc}} {{m4v}} viewer`

- Állítsa be a Findert a ftp:// URL-séma alapértelmezett kezelőjének:

`duti -s {{com.apple.Finder}} "{{ftp}}"`

- Az adott kiterjesztéshez tartozó alapértelmezett alkalmazásról szóló információk megjelenítése:

`duti -x {{ext}}`

- Az adott UTI alapértelmezett kezelőjének megjelenítése:

`duti -d {{uti}}`

- Egy adott UTI összes kezelőjének megjelenítése:

`duti -l {{uti}}`
