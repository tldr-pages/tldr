# AutoRaise

> Adds Focus Follows Mouse to Macos.
> Generates binary & app. standard options are available as standalone release.
> Add the binary or app to login item to start on boot.
> More information: <https://github.com/sbmpost/AutoRaise>.

- Compile the source code:

`make clean && make`

- Alternative options are available:

`make clean && make CXXFLAGS="-DOLD_ACTIVATION_METHOD -DEXPERIMENTAL_FOCUS_FIRST"`

- Default setup is documented in the readme, and shown on execution (the \& runs the process in the background, not necessary):

`autoraise &`
