# TorchBot|Find new friends
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)
## Developed for the project: [VBAZENRI](https://vk.com/vbazetrpg)
### Link to the bot: [Torch_bot](https://t.me/Torch_trpgbot)
## Features

- The bot uses google api to access google sheet, which stores user data, which is registered in VBAZENRI
- The bot offers the user a choice of types that it gets from Google Spreadsheets
- Using the selected types, the bot selects the people most suitable for the user
- And sends a list of contacts of these people
- Intermediate screening results are stored in sqlite database

### Telegram Bot is developed based on the pyTelegramBotAPI
##### and deployed on Heroku Cloud Service
##### Other libraries:
- asyncio
- google-api-python-client
- google-auth
- sqlite3
