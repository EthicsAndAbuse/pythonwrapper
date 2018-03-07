# pythonwrapper

To run the model and server, rasa **needs** to be installed and setup as per the [docs](https://rasa-nlu.readthedocs.io/en/latest/installation.html)

The rasa server has to be started before the Alana system is, as the pythonwrapper code will query the nonexistent api otherwise.

To start the rasa server:

`./start.sh`

To test the wrapper:

`python abusewrapper.py`

It will detect whether it is the main script or not so will behave accordingly
