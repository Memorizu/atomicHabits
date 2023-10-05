# AtomicHabit

AtomicHabit is an application that helps users improve their habits by sending notifications on Telegram about the habits they've created and need to perform.

## Installation

To install AtomicHabit and its dependencies, follow these steps:

1. Install [Poetry](https://python-poetry.org/docs/):

    ```sh
   curl -sSL https://install.python-poetry.org | python3 -
   
2. Clone the AtomicHabit repository:
    
    ```sh
          git clone <https://github.com/Memorizu/AtomicHabit.git>
          cd AtomicHabit
3. Install dependencies using Poetry:
    ```sh
    poetry install
   
Configuration
Create a .env file in the project root using .env.sample as an example. In this file, specify the following settings:

.env

    ADMIN_PASSWORD=
    SECRET_KEY=
    
    TELEGRAM_TOKEN=
    TELEGRAM_LINK=
    CELERY_RESULT_BACKEND=

## Usage

### Run the application:

    run python manage.py runserver
    Visit http://localhost:8000 in your browser.

Create a new habit, specifying its name and the time you want to receive notifications.

Receive notifications on Telegram about the habits you need to perform.
