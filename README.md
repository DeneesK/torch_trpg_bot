# TorchBot|Find new friends 
# Developed for the project: [VBAZENRI](https://vk.com/vbazetrpg)
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)
#### Telegram Bot is developed based on the pyTelegramBotAPI

##### Other libraries:
- asyncio
- google-api-python-client
- google-auth
- sqlite3

## Features

- The bot uses google api to access google sheet, which stores user data, which is registered in VBAZENRI
- The bot offers the user a choice of types that it gets from Google Spreadsheets
- Using the selected types, the bot selects the people most suitable for the user
- And sends a list of contacts of these people
- Intermediate screening results are stored in sqlite database
