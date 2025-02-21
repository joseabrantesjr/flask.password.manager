# Password Manager Documentation

Welcome to the **Password Manager** documentation! This project is a secure, encrypted password management web application built with Flask.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Security](#security)
- [Contributing](#contributing)
- [License](#license)

## Introduction

**Password Manager** is a web application developed in Python using the Flask framework. It securely stores and manages passwords using encryption provided by the **Fernet** library. Data is stored in an SQLite database.

## Installation

To install and set up **Password Manager**, follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/joseabrantesjr/flask.password.manager
```

### 2. Create a Virtual Environment

#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux:
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Generate a Secret Key

```bash
python key.py
```
Copy the generated key and add it to a `.env` file:

```bash
SECRET_KEY="YOUR_SECRET_KEY_HERE"
```

### 5. Run the Application

```bash
python run.py
```

Open your browser and go to `http://localhost:5000/`.

## Usage

Once the application is running, you can:

- Add new passwords
- View stored passwords
- Delete passwords securely

## Features

- **Encryption:** Passwords are stored securely using **Fernet encryption**.
- **Simple UI:** Intuitive interface for managing credentials.
- **Database Storage:** Uses SQLite for storing encrypted passwords.
- **Secure Key Management:** Keeps sensitive data protected.

## Security

- **All passwords are encrypted** before storage.
- **HTTPS recommended** for secure communication.
- **SECRET_KEY must be stored securely**—losing it will make all stored passwords inaccessible.

## Contributing

Contributions are welcome! If you'd like to improve **Password Manager**, follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make and test your modifications.
4. Submit a pull request.

## License

**Password Manager** is licensed under the **MIT License**.

[Read the full license](https://github.com/joseabrantesjr/flask.password.manager/blob/main/LICENSE).