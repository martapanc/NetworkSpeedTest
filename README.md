# NetworkSpeedTest
test your network's speed with a little bit of python
we completed this tool as part of Dr Brent Munsell's computer networking course

the tool is composed of two pieces: a gui client and a command-line server 
## server usage
```python speedy.py <portnum>```
then the magical code will listen for speed-test data coming in on the specified port and respond in a way that the client likes
that means both sending files when testing download speeds and receiving files when testing upload speeds