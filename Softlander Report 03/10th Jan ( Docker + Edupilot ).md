
All the issues of the docker images are fixed
## For MacOS and Linux

`docker-compose up -d`
- The container will start running with no problems
## For Windows

`docker-compose up -d`

-  Change the end-of-line sequence from CRLF to LF for the prestart.sh file.

![[Pasted image 20240110171736.png]]

- The container will now start running with no problems


# Edupilot interface

*make sure the docker container is running

http://localhost:8888 - opens the Edupilot interface

1) We first need to get an access token

![[Pasted image 20240110172415.png]]

Click on this

![[Pasted image 20240110172516.png]]

It returns a client secret after execution

![[Pasted image 20240110172600.png]]

2) Paste the access token in authorize 

![[Pasted image 20240110172646.png]]

3) Test the API calls ( admin has all privileges )

![[Pasted image 20240110173114.png]]