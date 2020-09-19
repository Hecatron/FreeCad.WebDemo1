# Client Side Development

## Building the ClientApp Sources

The ClientApp directory contains all the web / javascript / typescript related content.
The first step is to install all the needed libraries into the node_modules directory.
These are pulled from the package.json file in terms of names / versions etc.

With node package managers typically there is npm (vanilla) yarn (another popular one) and pnpm
I tend to use pnpm personally since it saves disk space by installing the libs into a directory such as D:\.pnpm-store\ then linking to them from there.

To install the sources
```
cd FreeCad.WebDemo1\ClientApp
pnpm install
```

Lets run a build (this defaults to development mode)
```
pnpm build
```

Webpack is used for the actual build.
In development mode the built files should include source maps for debugging within a web browser.
(this allows you to add breakpoints in vscode then have them hit / stop the code when a launched web browser reaches that point)

The destination files built typically end up within ..\wwwroot\dist\
There are 2 files

  * The vendor file is a collection of all the js related 3rd party libraries used
  * The main file is a collection of all the js code associated with the local site

Typically when debugging / running the main file is re-created on the fly as the Client side js / typescript code is changed.
This means you can just alter the Client side code (js / html / vue / etc) save it and have it auto re-load on the fly without having to stop / restart the debugging session.


## Browsing the web content outside of FreeCad

TODO
