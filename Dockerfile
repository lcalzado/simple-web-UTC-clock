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