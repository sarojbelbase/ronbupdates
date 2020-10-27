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

* TWEETARATI = 'The twitter username to get the tweets'
* CHANNEL= 'The telegram channel you want to send updates eg. @ronbupdates'
* SECRET_KEY= 'The secret key from flask.'
* BOT_TOKEN= 'Bot Token generated from @botfather on telegram'
* CONSUMER_KEY= 'Twitter's Consumer Key'
* CONSUMER_SECRET='Twitter's Consumer Secret Key'
* ACCESS_KEY= 'Twitter's Access Key'
* ACCESS_SECRET= 'Twitter Access Secret Key'
* DATABASE_URL=' Database either sqlite or postgres eg: postgres://abcdef:ghijklmn@opqrstuv:5432/wxyz'

### Run & Setups

* Install & Activate virtual environment in this folder
* `pip3 install -r requirements.txt`

#### Local:

`flask run app.py`

#### Production:

`gunicorn -b 0.0.0.0:8000 app:app --log-level debug`

### Links

<strong><a target="_blank" href="https://ronb.glitch.me/">web > ronb.glitch.me</a></strong><br>
<strong><a target="_blank" href="https://t.me/routineofnepalbot">telegram bot > t.me/routineofnepalbot</a></strong><br>
<strong><a target="_blank" href="https://t.me/updatesfromronb">telegram channel > t.me/updatesfromronb</a></strong><br>


### Made with ❤️ in Nepal. 


