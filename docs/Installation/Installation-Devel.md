# Installation

## Development Depends

### Installing ptvsd

For debugging the python side of things when using Visual Studio Code
there are two debuggers available

  * ptvsd - this is the older debugger that was replaced around March
  * debugpy - this is the newer debugger that is currently used

There is however an issue / pull request for debugpy for when used within an application that embeds Python
(which is something that FreeCad does

  * https://github.com/microsoft/debugpy/issues/262
  * https://github.com/microsoft/debugpy/pull/387

So for now I'll install both but use ptvsd untill debugpy has been fixed.

Launch the python.exe within the freecad install (make sure it's running as administrator)
```
import pip;
pip.main(['install'] + ['ptvsd']);
pip.main(['install'] + ['debugy']);
```

There is supposed to be an inbuilt debugger of
```
from freecad.gui import RemoteDebugger
RemoteDebugger.attachToRemoteDebugger()
```

However I seem to have issues with getting this working with the latest 0.19 dev release
```
ImportError: bad magic number in 'freecad': b'\x03\xf3\r\n'
```


### Installing python linting

For linting / code style highlighting within vscode

Launch the python.exe within the freecad install (make sure it's running as administrator)
```
import pip;
pip.main(['install'] + ['pep8']);
pip.main(['install'] + ['pycodestyle']);
pip.main(['install'] + ['pylint']);
pip.main(['install'] + ['flake8']);
pip.main(['install'] + ['coverage']);
```
