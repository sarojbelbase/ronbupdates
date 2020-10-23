from ronb import create_app, db
from ronb.models import Info, Tweet

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'Info': Info, 'Tweet': Tweet, 'db': db}


if __name__ == '__main__':
    app.run(debug=True)
