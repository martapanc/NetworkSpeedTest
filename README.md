# NetworkSpeedTest
## team venomous ninjas
test your network's speed with a little bit of python
we completed this tool as part of Dr Brent Munsell's computer networking course

the tool is composed of two pieces: a gui client and a command-line server 
## usage
###server
```python speed.py <portnum> server```
then the magical code will listen for speed-test data coming in on the specified port and respond in a way that the client likes
that means both sending files when testing download speeds and receiving files when testing upload speeds

by default, the client uses port 8080. 

to test the client side:
```python speed.py <serverIP> <number of bytes to transfer>```

###gui
simply launch it (`python GUI.py`), enter your server's information, and start testing

## deliverables
1. [presentation](https://docs.google.com/presentation/d/1wtkUrT7rsp_aM1Gm9MfwR15F5VKcbG8NarQNsRT8pCc/edit?usp=sharing)
2. [design document](./finalDesignDoc.docx)
3. ![nic cage](https://stubbornthoughts.files.wordpress.com/2013/01/tumblr_m3fc1bghyt1rq84v4o1_1280.png)