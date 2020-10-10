# Finance Tracking

## Description
The goal of this project is to provide users an insight into how much they're spending over a period of time along with the distribution of money that is spent on particular things (Shopping, Car Expenses, Misc., etc.) along with tracking how much money they're having come in each month.
This information should be determined given a CSV file formatted to match the expected formatting. Most banks allow you to export a CSV report which is why I went with this. 

## Getting Started

## Items needed for building this project
* Python3 (3.6+)
* Pipenv
* Docker (mysql image)
* NodeJS
* Node Package Manager (NPM)
* Typescript (3+)
* Angular 9 CLI

## Setting up/Running mysql image
1) Pull latest mysql image ```docker pull mysql:latest```
2) Run the container and initialize with root password ```docker run --name mysql -e MYSQL_ROOT_PASSWORD=Test123 -e MYSQL_DATABASE=FinanceTracking -d mysql:latest``` --name will be the name of the container
3) Ensure the docker port default is port 3306

## Running FinanceTrackingAPI
1) Move into the FinanceTrackingAPI directory
2) Run ```pipenv shell``` to launch subshell in virtual environment
3) Inside the shell of the virtual environment run ```pipenv install``` to install dependencies
4) Inside the shell of the virtual environment run ```python -m src.main``` to start the flask API

## Running FinanceTrackingUI
1) Move into the FinanceTrackingUI directory
2) I personally like to run ```npm install``` to ensure I have all the packages needed for the angular project.
3) After that run ```npm start``` or ```ng serve``` to start running the Angular application locally, refer to the [README.md](FinanceTrackingUI/README.md) in the FinanceTrackingUI directory for additional information and commands related to running the Angular application.

## Future Enhancements
**This is still a work in progress.**
* Give users ability to enter specific information without having to put it into a CSV and upload it.
* Currently this only accepts a specifically formatted CSV, it can be expanded to possibly accept PDF's or different formattings of CSVs.
