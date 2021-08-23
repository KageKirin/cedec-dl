## Quick JSON Parser hack

# namespace: qjph
from pathlib import Path

def load(filename):
    return loads(Path(filename).read_text())

def loads(s):
    ## quick JSON parser hack
    gg = globals()
    gg.update({
        'true': True,
        'false': False,
    })
    return eval(s, gg)
