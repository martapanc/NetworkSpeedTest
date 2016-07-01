# NetworkSpeedTest
## Team 'Venomous Ninjas'
Test your network's speed with a little bit of Python.
We completed this tool as part of Dr Brent Munsell's computer networking course, at College of Charleston (CSCI440 - Computer Networks, Fall 2015).

The tool is composed of two pieces: a GUI client and a command-line server.
## Usage
###Server
```python speed.py <portnum> server```
Then the magical code will listen for speed-test data coming in on the specified port and respond in a way that the client likes.
That means both sending files when testing download speeds and receiving files when testing upload speeds.

By default, the client uses port 8080. 

To test the client side:
```python speed.py <serverIP> <number of bytes to transfer>```

###GUI
Simply launch it (`python GUI.py`), enter your server's information, and start testing.

## Deliverables
1. [Presentation](https://docs.google.com/presentation/d/1wtkUrT7rsp_aM1Gm9MfwR15F5VKcbG8NarQNsRT8pCc/edit?usp=sharing)
2. [Design document](./finalDesignDoc.docx)
3. ![nic cage](https://stubbornthoughts.files.wordpress.com/2013/01/tumblr_m3fc1bghyt1rq84v4o1_1280.png)
