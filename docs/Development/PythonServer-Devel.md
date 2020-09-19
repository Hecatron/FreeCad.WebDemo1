# Python / Server Development

  * https://wiki.freecadweb.org/Debugging#Python_Debugging
  * https://forum.freecadweb.org/viewtopic.php?f=10&t=35383

## Using VSCode

  * https://forum.freecadweb.org/viewtopic.php?p=372496
  * https://code.visualstudio.com/docs/python/debugging#_debugging-by-attaching-over-a-network-connection

```
import ptvsd;
ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True);

# This might be better
ptvsd.enable_attach(address=('localhost', 5678));

# Wait for vscode to attach
ptvsd.wait_for_attach();
```

### VSCode configuration

launch.json
```
    "configurations": [
        {
            "name": "Server: Attach to FreeCad",
            "type": "python",
            "request": "attach",
            "port": 5678,
            "host": "localhost",
            "pathMappings": [
                {
                    "localRoot": "${workspaceFolder}",
                    "remoteRoot": "."
                }
            ],
            "debugOptions": [
                "RedirectOutput"
            ]
        },
    ]
```
