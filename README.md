# FourWheels

FourWheels is a Python-Django app that is used to blur the number plate from the images of the given vehicles using Python's libraries.

## Prerequisite
You must have the below-mentioned minimum requirements to start the project.
- **Pip**: 23.2.1
- **Python**: 3.8.10
- **Django**: 4.2.1
- **Django Rest Framework**: 3.14.0
- **Database**: MySql || Postgresql
- **Libraries**: python-dotenv, numpy, opencv-python

## Installation

Follow the following guidelines to install the project using command line.

#### Libraries Installation
```bash
pip install numpy
pip install opencv-python
pip install python-dotenv
```
#### Database Installation
Install DB according to your choice.
```bash
pip install mysqlclient     #MySql
pip install psycopg2        #Postgresql
```

## Setup
#### Clone
Open the terminal & clone it by using the following command.
```bash
https://github.com/faisal-shehzad-dev/FourWheels.git
```


#### DB setup
- Create the root user for MySql/Postgresql.
- Create the database for the project.


#### Env setup
- Create .env in the project root directory.
- Setup the environment variables according to the **.env.example**
- Setup the port according to the database.


## Project Run
- Go to the project directory **FourWhells**.
- Open the terminal & type the following commands
```bash
    python manage.py migrate        #Migrate the DB
    python manage.py runserver      #Run the server
```
- Open the browser & in the search bar hit the below link & enjoy.
- [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


## Database Console
- Open the terminal & use the following command to open the console
```bash
    python manage.py shell        #Open the db console
```

## API Reference
The end point for APIs is at the given link.
- [API Documentation](https://github.com/faisal-shehzad-dev/FourWheels/blob/main/docs/ROUTES.md)

## Contributing
Pull requests are welcome.
- Create a PR from the main branch.
- Follow the code style & flow.
- Follow the PR guidelines.
- Approve the PR then merge it.
- Update the documentation & read me.
- Become a contributor.


## License

- This license is issued and maintained by the open-source developer's team.
