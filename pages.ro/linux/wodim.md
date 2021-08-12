# wodim

> Comandă (aliasată ca `cdrecord` pe unele sisteme) pentru înregistrarea datelor pe CD-uri sau DVD-uri.
> Unele invocări ale wodim pot provoca acțiuni distructive, cum ar fi ștergerea tuturor datelor de pe un disc.

- Display-uri optice disponibile pentru `wodim`:

`wodim --devices`

- Înregistrarea („inscripționarea”) a unui disc numai audio:

`wodim dev=/dev/{{optical_drive}} -audio {{track*.cdaudio}}`

- Ardeți un fișier pe un disc, ejectând discul odată făcut (unele înregistratoare necesită acest lucru):

`wodim -eject dev=/dev/{{optical_drive}} -data {{file.iso}}`

- Inscripționarea unui fișier pe disc într-o unitate optică, potențial scrierea pe mai multe discuri succesiv:

`wodim -tao dev=/dev/{{optical_drive}} -data {{file.iso}}`
