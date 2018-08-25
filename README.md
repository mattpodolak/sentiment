- [Getting Started](#getting-started)
    - [Creating Project](#creating-project)
    - [Setting Up](#setting-up)
    - [Running Your App](#running-your-app)

# Getting Started

## Creating Project
```bash
> git clone https://github.com/mattpodolak/sentiment.git
> git remote add origin https://github.com/mattpodolak/sentiment.git
```

## Setting Up
Make new venv
```bash
> python -m venv sentiment-venv
```

Activate venv
```bash
> sentiment-venv\Scripts\activate
> source sentiment-venv/bin/activate // for Mac users
```

Install required packages
```bash
> pip install -r requirements.txt
```

## Running your app
Activate venv (if not already activated) and run
```bash
> sentiment-venv\Scripts\activate
> flask run
```