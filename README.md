# Password Manager - An encrypted password management application

## Introduction

**Password Manager** is a web application developed in Python using the Flask framework that allows the user to store and manage their passwords in a secure and encrypted way. The application uses the Fernet library to encrypt passwords and the SQLite database to store them.

## Installation

To install **Password Manager**, follow these steps:

1. Install Python and pip on your system.

2. Clone this repository using the command.

``` bash
git clone https://github.com/joseabrantesjr/flask.password.manager
```

3. Create and activate a virtual environment (venv)

Step 1:
In the terminal, use the python -m venv command to create a virtual environment. Replace <environment_name> with the desired name for your virtual environment.

```bash
python -m venv venv
```
Step 2: Activate the Virtual Environment

After creating the virtual environment, you need to activate it to use it for your project. The method for activating the environment depends on your operating system.

On Windows:

```bash
venv\Scripts\activate
```
On macOS e Linux:

```bash
source venv/bin/activate
```


4. Enter the root directory of the project and run 
``` bash
pip install -r requirements.txt
``` 
or `pip3 install -r requirements.txt`
to install all the necessary dependencies.

5. Open the app folder and run python 
``` bash
python secret.key.generator.py
```
or `python3 secret.key.generator.py`
, a security key will be generated so you can insert it in the config.py file (SECRET_KEY = b' insert the secret key here ')

6. Run 
``` bash
python run.py
``` 
or `python3 run.py` to start the Flask development server.

# Usage

To use **Password Manager**, open a command line interface or terminal and navigate to the root folder of the project. Run `python run.py` or `python3 run.py` to start the Flask development server. Then open a browser and go to `http://localhost:5000/` to access the application.

## Functions

**Password Manager** offers the following functions:

- **Add password:** To add a new password, you will need to fill in a form with the name of the password, the username and the password itself. The password will be encrypted before being stored in the database.

- **View Password:** You can view an existing password by clicking a view button on the main page. This will display the encrypted password on the screen.

- **Delete Password:** To delete a password, you will need to select the desired password on the main page and click a confirmation button. This will delete the password from the database.

## Security

Security is an important concern for **Password Manager**. Therefore, the application uses the Fernet library to encrypt passwords before storing them in the database. In addition, the application uses HTTPS to ensure that information is transmitted securely between the client and the server.

## Contributions

Everyone is welcome to contribute to **Password Manager**. If you find any bugs or want to add new features, please fork this repository, make the necessary changes and submit a pull request.

## License

**Password Manager** is licensed under the MIT License. You can read the full license at [https://opensource.org/licenses/MIT](https://opensource.org/licenses/MIT).
