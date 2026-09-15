# slideshow

> Make presentation slides in the Racket language.
> More information: <https://docs.racket-lang.org/slideshow>.

- Display a default slide with options to run the tutorial or load a `.rkt` presentation file:

`slideshow`

- Start a presentation in full screen:

`slideshow {{path/to/presentation.rkt}}`

- Display the presentation window with a title bar and resize border:

`slideshow --keep-titlebar {{path/to/presentation.rkt}}`

- Set the width and height (in pixels) of the presentation window:

`slideshow {{[-s|--size]}} {{width}} {{height}} {{path/to/presentation.rkt}}`

- Export a presentation to a PDF file:

`slideshow {{[-D|--pdf]}} -o {{path/to/presentation.pdf}} {{path/to/presentation.rkt}}`
