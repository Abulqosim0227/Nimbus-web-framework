from Nimbus.app import Nimbusapp
from Nimbus.middleware import Middleware

# Initialize the Nimbusapp instance
app = Nimbusapp()

# Route for Home Page
@app.route("/home", allowed_methods=["get"])
def home(request, response):
    response.text = "Hello from the Home Page"

# Route for About Page
@app.route("/about", allowed_methods=["put"])
def about(request, response):
    response.text = "Hello from the About Page"

# Route for dynamic greeting with a name parameter
@app.route("/hello/{name}")
def greeting(request, response, name):
    response.text = f"Hello {name}"

# Class-based route for Books page
@app.route("/books")
class Books:
    def get(self, request, response):
        response.text = "Books page"

    def post(self, request, response):
        response.text = "Endpoint to create a book"

# New handler route without a class
@app.route("/new_handler")
def new_handler(request, response):
    response.text = "From new handler"

# Route for rendering templates
@app.route("/template")
def template_handler(request, response):
    response.html = app.template(
        "test.html",  # Ensure this file exists in your templates folder
        context={"new_title": "Best Title", "new_body": "Best body"},
    )

# Route for JSON response
@app.route("/json")
def json_handler(req, resp):
    response_data = {"name": "some name", "type": "json"}
    resp.json = response_data

# Exception handling route to catch errors
def on_exception(req, resp, exc):
    resp.text = f"Error occurred: {exc}"

app.add_exception_handler(on_exception)

# Route to throw an exception for testing the exception handler
@app.route("/exception")
def exception_throwing_handler(req, resp):
    raise AttributeError("This is a test exception")

# Middleware to log requests and responses
class LoginMiddleware(Middleware):
    def __init__(self, app):
        super().__init__(app)

    def process_request(self, req):
        print(f"Request URL: {req.url}")

    def process_response(self, req, resp):
        print(f"Response generated for URL: {req.url}")

app.add_middleware(LoginMiddleware)

# Run the application with waitress server
if __name__ == "__main__":
    from waitress import serve

    print("Starting server at http://127.0.0.1:8000")
    serve(app, host="127.0.0.1", port=8000)