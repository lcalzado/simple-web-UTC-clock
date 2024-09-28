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
