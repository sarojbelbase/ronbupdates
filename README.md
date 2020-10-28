<p align="center">
<img src="./ronb/static/ronb.png" width="22%" height="auto"><br>
<strong>
A telegram-bot that sends <a href="https://www.facebook.com/officialroutineofnepalbanda/">Routine Of Nepal Banda</a> updates from <a href="https://twitter.com/RONBupdates">twitter</a> as they happen.
</strong>
</p>


### Screenshots

<span align="center">
<img src="./ronb/static/one.jpg" width="49%" height="auto">
<img src="./ronb/static/two.jpg" width="49%" height="auto">
</span><br>

### Overview

This is just a simple bot that has capability of sending stuffs to channel or groups or any account you like. You could use this bot to whatever stuffs you like. But as an example, I made it to work with a channel only. Setting this project was hard this time, since it involves a database. [I have worked with a telegram-bot in the past](https://github.com/sidbelbase/covidnepal-bot) but during this project, I came across several challenges like cron jobs, python wrappers, VPS servers, etc.

I tried integrating various wrappers like [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot), [aiogram](https://github.com/aiogram/aiogram), [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI), etc. **But in the end, I went all-bare i.e worked from the scratch**. Setting my own webhook, sending photos my own way, sending messages like I want. I have a database placed in middle so that could be used for keeping records or a vue-based news client in the future maybe. I have also posted Github-gists below for individual breaking down of these stuffs & most important part for now, the bot won't be able to reply you, because it's busy doing works appointed by me. You could fork this one and make it work like you wanted. If you find this useful, please email me or create an issue, so that I would know you liked it so much or you may just give it a star. Yes, a star would be fine. Peace!!!

### Prerequisites

* Python 3 or higher
* Twitter Account with Developer Access
* Telegram Account
* SQLite / Postgres Database

### Used Tools & Technologies

* tweepy : Twitter for Python!
* flask : Python framework for building web applications
* postgresql : A object-relational database system
* sqlalchemy : SQL toolkit and object-relational mapper for Python

### Environment Variables

* `TWEETARATI`= 'The twitter username to get the tweets'
* `CHANNEL` = 'The telegram channel you want to send updates eg. @ronbupdates'
* `SECRET_KEY` = 'The secret key from flask.'
* `BOT_TOKEN` = 'Bot Token generated from @botfather on telegram'
* `CONSUMER_KEY` = 'Twitter's Consumer Key'
* `CONSUMER_SECRET`= 'Twitter's Consumer Secret Key'
* `ACCESS_KEY` = 'Twitter's Access Key'
* `ACCESS_SECRET` = 'Twitter Access Secret Key'
* `DATABASE_URL` = 'Database either sqlite or postgres eg: postgres://abcdef:ghijklmn@opqrstuv:5432/wxyz'

### Run & Setups

* [Install & activate virtual environment in this folder](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)
* Add `.env` file in this folder & add environment variables given aboove
* Run `pip3 install -r requirements.txt`

#### Local:

`flask run app.py`

#### Production:

`gunicorn -b 0.0.0.0:8000 app:app --log-level debug`

### Links

<strong><a target="_blank" href="https://ronb.glitch.me/">web > ronb.glitch.me</a></strong><br>
<strong><a target="_blank" href="https://t.me/routineofnepalbot">telegram bot > t.me/routineofnepalbot</a></strong><br>
<strong><a target="_blank" href="https://t.me/updatesfromronb">telegram channel > t.me/updatesfromronb</a></strong><br>

### Gists

<strong><a target="_blank" href="https://gist.github.com/sidbelbase/74db2176cfcd686bcacfb14386796359">fetch_tweets.py</a></strong><br>
<strong><a target="_blank" href="https://gist.github.com/sidbelbase/383744970eb684941b314e95667c37bd">models.py</a></strong><br>

### Disclaimer
 
 This bot or channel is not associated with either **Routine of Nepal Pvt. Ltd.** or [ronbpost](https://ronbpost.com/) , it is only made for informational purpose on widely adopted messaging platform i.e [Telegram](https://telegram.org).


### Made with ❤️ in Nepal. 


