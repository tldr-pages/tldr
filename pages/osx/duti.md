# duti

> Set default applications for document types and URL schemes on macOS.

- Set Safari as the default handler for HTML documents:

`duti -s {{com.apple.Safari}} {{public.html}} all`

- Set VLC as the default viewer for files with .m4v extensions:

`duti -s {{org.videolan.vlc}} {{m4v}} viewer`

- Set Finder as the default handler for the ftp:// URL scheme:

`duti -s {{com.apple.Finder}} {{ftp}}`

- Display information about the default application for a given extension:

`duti -x {{ext}}`

- Display the default handler for a given UTI:

`duti -d {{uti}}`

- Display all handlers of a given UTI:

`duti -l {{uti}}`
