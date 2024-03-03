## Working-Memory-CAS
# Code Style:
    Methods inside frame classes:
        Tkinter widgets: __widget type_name
        Private frame-specific methods: __name
    Attributes inside frame classes:
        Tkinter instances: widget type_name
    *All other naming should follow python code style

    Placement of code blocks inside frame classes:
        __init__
        tkinter widgets
        ...
        __button
        other methods

    All data processing should be done within frame classes/instances
    Avoid handling any data main.py

# TODO:
    1. color


Dependencies:
    1. pillow 
        pip intall pillow
    2. Python3.9+
    3. numpy
        pip install numpy