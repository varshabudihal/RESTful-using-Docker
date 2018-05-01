# RESTful website using Docker
Created a RESTful Web service that displays data in JSON format using two get routes : 
   
   1)/food
   
   2)/food/id
    
Steps:

-Setup the project with the app.py and JSON file in a single folder.

-In the docker terminal, use command "touch Dockerfile" to create the Dockerfile and setup the DockerFile accordingly.

-Create Docker Image by running : "docker build -t flask-image:latest ."

-You can check the image created using "docker images"

-Run the app image inside a container using "docker run -d -p 5000:5000 --name flask-container flask-image" 

-Check running docker container by "docker ps"

-App will now be running at this address : http://192.168.99.100:5000/food
