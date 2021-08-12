# tldr

> Afișează pagini de ajutor simple pentru instrumente de linie de comandă, din proiectul tldr-pages.
> Mai multe informaţii: <https://tldr.sh>

- Afișați pagina tldr pentru o comandă (indiciu: acesta este modul în care ați ajuns aici!) :

`tldr {{command}}`

- Afișează pagina tldr pentru `cd`, suprascriind platforma implicită:

`tldr -p {{android|linux|osx|sunos|windows}} {{cd}}`

- Afișează pagina tldr pentru o subcomandă:

`tldr {{git-checkout}}`

- Actualizați paginile locale (dacă clientul acceptă memorarea în cache):

`tldr -u`
