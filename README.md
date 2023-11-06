# file-uploader

![Diagram](doc/medidoc.png?raw=true "Diagram")


A flask microservice that receives file uploads and publishes 
them to an MQTT topic.

File-uploader is the frontend for the Medidoc project. It exposes an
interface to upload files of various types and link them with an external
ID that the user can specify.

Uploaded files are published to an MQTT topic, which is then consumed
by the file-processor microservice and processed.

File-uploader allows the user to query the file-processor microservice
and browse processed files.

## How to run

Use the attached docker-compose.yaml to run file-uploader with all of it's
service dependencies. Once the containers are up, access the frontend at
http://localhost:5000

If you make changes to the source, you can run:

    docker-compose up -d --build

This will redeploy the containers with the new code. In case one of
the other service dependencies are updated, make sure to run:

    docker pull <image>
    docker compose up -d --build

This will deploy the new images.

This application was written as part of an assignment to complete the 
Computer Science Master of Science degree at IUBH.

Ivan Šarić - 2023
