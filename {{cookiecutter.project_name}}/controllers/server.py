import os
from waitress import serve
from train_app import app

if __name__ == "__main__":
    app.debug = True
    server = os.getenv("SERVER")
    port = os.getenv("PORT")
    serve(app, host=server, port=port)
