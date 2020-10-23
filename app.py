from ronb import create_app, db
from ronb.models import Info, Tweet
from os import environ

app = create_app()
port = int(environ.get('PORT', 5000))
host = "0.0.0.0"


@app.shell_context_processor
def make_shell_context():
    return {'Info': Info, 'Tweet': Tweet, 'db': db}


if __name__ == '__main__':
    app.run(debug=True, host=host, port=port)
