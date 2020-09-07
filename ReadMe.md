# Finance Tracking

## Getting Started

## Items needed for building this project
* Python3 (3.6+)
* Docker (mysql image)
* NodeJS
* Typescript (3+)
* Angular 9 CLI

## Setting up/Running mysql image
1) Pull latest mysql image ```docker pull mysql:latest```
2) Run the container and initialize with root password ```docker run --name mysql -e MYSQL_ROOT_PASSWORD=Test123 -d mysql:latest``` --name will be the name of the container
3) Change access URL ports to 8080 (docker port default is port 3306)
4) Add Environment variable to the container to ensure database is initialized on load. **Key**: MYSQL_DATABASE - **Value**: FinanceTracking

## Running FinanceTrackingAPI
1) Move into the FinanceTrackingAPI directory
2) Run ```pipenv shell``` to launch subshell in virtual environment
3) Inside the shell of the virtual environment run ```python -m src.main``` to start the flask API

## Running FinanceTrackingUI
1) Move into the FinanceTrackingUI directory
2) I personally like to run ```npm install``` to ensure I have all the packages needed for the angular project.
3) After that run ```npm start``` or ```ng serve``` to start running the Angular application locally, refer to the [README.md](FinanceTrackingUI/README.md) in the FinanceTrackingUI directory for additional information and commands related to running the Angular application.