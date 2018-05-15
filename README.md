# EmailParser
A python2 script that is used to parse emails to lists, each list belongs to a domain.


the script supports 2 methods to save the result:

1-All in 1 file

the result will something be like this:
```
gmail.com:

awd@gmail.com
awdawd@gmail.com
....
##################
yahoo.com:
......
......
##################
```

2-Each domain to a file

the script will create a file for each domain and save it's emails in it.
```
kendoclaw1@kendoclaw1:~/bin$ python emailparser.py -h
usage: emailparser.py [-h] [-f FILE] [-o PATH] [-i]

Email Parser

optional arguments:
  -h, --help  show this help message and exit
  -f FILE     file that contains emails
  -o PATH     Path to save the results
  -i          Create a file for each domain and save emails in it
[-] Usage: python emailparser.py -h
```


