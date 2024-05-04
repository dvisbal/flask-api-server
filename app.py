import json

from flask import Flask, redirect, url_for

app = Flask(__name__)

example_of_saving_a_global_variable_that_can_be_shared_between_requests = []

@app.route('/')
def hello_geek():
    return 'Hello from Flask'

@app.route('/redirect/')
def redirect():
    return redirect(url_for('redirect_to_here', example_url_parameter="This is an example url parameter"))

@app.route('/redirect/<example_url_parameter>')
def redirect_to_here(example_url_parameter):
    example_of_saving_a_global_variable_that_can_be_shared_between_requests.append(
        example_of_saving_a_global_variable_that_can_be_shared_between_requests[-1] + 1
    )
    return json.dumps({
        "This route is converting a dict to json": {
            "And this is a string that was passed from the original url to the redirect url as a url parameter": 
                example_url_parameter
        },
        "example_of_saving_a_global_variable_that_can_be_shared_between_requests": 
            example_of_saving_a_global_variable_that_can_be_shared_between_requests
    })

@app.route('/reset')
def reset():
    example_of_saving_a_global_variable_that_can_be_shared_between_requests.clear()
    return "reset, and this is an example of returning a string instead of json"

if __name__ == "__main__":
    app.run(debug=True)