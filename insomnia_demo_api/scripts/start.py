from insomnia_demo_api.app import app


def run(debug=False):
    app.run(port=8080, debug=debug, server='flask')


def run_debug():
    run(debug=True)
