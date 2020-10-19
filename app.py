from ronb import create_app, db
from ronb.models import Tweet

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db,  'Tweet': Tweet}


if __name__ == '__main__':
    app.run(debug=True)
