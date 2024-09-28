# Simple Web UTC Clock

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

### adding the dockerfile

I added 2 more files to this structure the requirements file and the dockerfile.

1. The requirements.txt file have all dependencues declarations:
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
