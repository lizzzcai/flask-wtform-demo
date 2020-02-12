"""Initialize app."""
from flask import Flask


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    app.config['RECAPTCHA_PUBLIC_KEY'] = 'iubhiukfgjbkhfvgkdfm'
    app.config['RECAPTCHA_PARAMETERS'] = {'size': '100%'}

    with app.app_context():
        # Import parts of our application
        import routes

        return app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)