# Demonstrates a bug with sending binary data to Python Azure Functions

* Run the Function app in the Functions folder using the local functions host
* Launch the `app.py` file using Python3
* The size of the file that is sent as binary data is 265,160 bytes
* The size of the body received by the function app is 476,550 bytes
* Saving the body data as an image leads to an invalid jpg