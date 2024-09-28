# Simple Web UTC Clock

## Pre-requisites
Docker installed on your system

## Introductions
Here I share a simple web app that I created, a UTC clock.But the 
focus of this repository is how to build and deploy it.

### Application description
This app shows the Coordinated Universal Time (UTC) using python, flask and dockers.

**This is the flask structure:**
```
/simple-web-UTC-clock
    clock.py
    /templates
        index.html
    /static
        script.js
        styles.css
```

### Adding the Dockerfile

I added 2 more files to this structure the requirements file and the Dockerfile.

1. The requirements.txt file have all dependencies declarations:
```
Flask
```

2. The dockerfile contains all the steps to be executed each time we create an instance of the built image:

```
#Base image
FROM python:3.12-alpine

#Set the working dir in the container
WORKDIR /clock

#Copy the content of the current dir into the container at /clock
COPY . /clock/

#Install dependencies defined on the requirements file
RUN pip install --no-cache-dir -r requirements.txt

#Make the container listen on port 5000
EXPOSE 5000

#Run the application when the container starts.
CMD ["python3", "clock.py"]
```

**Final structure**

The final directory structure is as follows:
```
/simple-web-UTC-clock
    requirements.txt
    Dockerfile
    clock.py
    /templates
        index.html
    /static
        script.js
        styles.css
```

**Creating the image and running an instance**

To create an image of the app run the command inside the the project directory (/simple-web-UTC-clock):
```
sudo docker build -t [image-name] .
```
In my case I used:
```
sudo docker build -t lcalzado/simple-web-clock .

To run an instance of you app use the command:
```
docker run -d -p 80:5000 --name web-clock lcalzado/simple-web-clock
```
This command create a container named web-clock mapping the port 80 in the host to the 5000 port
in the container on detach mode.
```

**Extra**

If you want to run an instace that shows you local time insted of the UTC you can use the following command:
```
docker run -d -e TZ=$(cat /etc/timezone) -p 5000:5000 --name web-clock-local lcalzado/web-clock
```
Here I add an extra option "-e" which stands for enviroment variable.
It adds your localhost timezone into the container timezone. 


I hope this have been informative for you and I'd like to thank you for reading it.
