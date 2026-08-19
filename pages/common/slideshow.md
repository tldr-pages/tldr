# slideshow

> Tool to make presentation slides, part of Racket language ecosystem.
> More information: <https://docs.racket-lang.org/slideshow>.

- Display a default slide with options to run the tutorial or load a `.rkt` presentation file:

`slideshow`

- Show a presentation in full screen:

`slideshow {{path/to/presentation.rkt}}`

- Instead of full screen, give the presentation slide window a title bar and resize border:

`slideshow --keep-titlebar {{path/to/presentation.rkt}}`

- Set width and height (in pixels) of presentation slide window:

`slideshow -s {{width}} {{height}} {{path/to/presentation.rkt}}`

- Save presentation in PDF file format:

`slideshow --pdf -o {{path/to/presentation.pdf}} {{path/to/presentation.rkt}}`
