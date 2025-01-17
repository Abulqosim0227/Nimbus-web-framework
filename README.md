I’ve reviewed your repository and the `README.md` file. Below is an updated and improved version of your `README.md` that is better structured, more professional, and includes all the necessary information for users to understand and use your project.

---

### **Updated `README.md`**
```markdown
# Nimbus Web Framework

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Version](https://img.shields.io/badge/version-0.1.0-orange)
![PyPI](https://img.shields.io/pypi/v/nimbus-web-framework)
![GitHub Stars](https://img.shields.io/github/stars/Abulqosim0227/Nimbus-web-framework?style=social)
![GitHub Issues](https://img.shields.io/github/issues/Abulqosim0227/Nimbus-web-framework)

**Nimbus** is a lightweight Python web framework designed for simplicity and performance. Built for learning purposes, it provides essential features like routing, middleware support, template rendering, and static file serving.

---

## Features

- **Easy Routing**: Define routes with support for dynamic URL parameters.
- **Middleware Support**: Add custom middleware for request/response processing.
- **Template Rendering**: Use Jinja2 templates for dynamic HTML content.
- **Static File Serving**: Serve static files (CSS, JS, images) with WhiteNoise.
- **JSON Responses**: Easily return JSON data from your routes.
- **Exception Handling**: Custom exception handlers for better error management.

---

## Installation

You can install **Nimbus Web Framework** via pip:

```bash
pip install nimbus-web-framework
```

---

## Quick Start

### 1. Create a Simple App

```python
from nimbus import Nimbusapp

app = Nimbusapp()

@app.route("/")
def home(request, response):
    response.text = "Hello, World!"

if __name__ == "__main__":
    app.run()
```

### 2. Run the App

Start the development server:

```bash
python app.py
```

Visit `http://localhost:8080` in your browser to see "Hello, World!".

---

## Basic Usage

### Routing

Define routes with the `@app.route` decorator:

```python
@app.route("/about")
def about(request, response):
    response.text = "About Us"
```

### Dynamic Routes

Capture URL parameters:

```python
@app.route("/hello/{name}")
def greet(request, response, name):
    response.text = f"Hello, {name}!"
```

### Template Rendering

Use Jinja2 templates to render HTML:

```python
@app.route("/template")
def template_handler(request, response):
    response.html = app.template(
        "test.html",
        context={"title": "Nimbus", "message": "Welcome to Nimbus!"}
    )
```

### Static Files

Serve static files (CSS, JS, images) from the `static/` directory:

```html
<link rel="stylesheet" href="/static/styles.css">
```

### JSON Responses

Return JSON data:

```python
@app.route("/json")
def json_handler(request, response):
    response.json = {"status": "success", "message": "Hello, JSON!"}
```

### Middleware

Add custom middleware:

```python
class LoggingMiddleware:
    def __init__(self, app):
        self.app = app

    def process_request(self, req):
        print(f"Request: {req.url}")

    def process_response(self, req, resp):
        print(f"Response: {resp.status_code}")

app.add_middleware(LoggingMiddleware)
```

---

## Testing

The framework includes a comprehensive test suite to ensure functionality. To run the tests:

1. Clone the repository:
   ```bash
   git clone https://github.com/Abulqosim0227/Nimbus-web-framework.git
   cd Nimbus-web-framework
   ```

2. Install the development dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the tests:
   ```bash
   pytest tests/test_app.py
   ```

### Example Test File (`test_app.py`)

```python
import pytest
from nimbus import Nimbusapp

@pytest.fixture
def app():
    return Nimbusapp()

@pytest.fixture
def test_client(app):
    return app.test_session()

def test_basic_route_adding(app, test_client):
    @app.route("/home")
    def home(req, resp):
        resp.text = "Hello from home"

    response = test_client.get("https://testserver/home")
    assert response.text == "Hello from home"

def test_template_handler(app, test_client):
    @app.route("/template")
    def template(req, resp):
        resp.html = app.template(
            "test.html",
            context={"title": "Nimbus", "message": "Welcome to Nimbus!"}
        )
    response = test_client.get("https://testserver/template")
    assert "Welcome to Nimbus!" in response.text
```

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Inspired by **Flask** and **Bottle**.
- Built with ❤️ by [Abulqosim Rafiqov](https://github.com/Abulqosim0227).

---

## Support

If you have any questions or need help, feel free to open an issue on [GitHub](https://github.com/Abulqosim0227/Nimbus-web-framework/issues).

```

---

### **Key Improvements**
1. **Badges**:
   - Added badges for Python version, license, version, PyPI, GitHub stars, and issues.
   - These badges make your project look professional and provide quick insights.

2. **Installation Instructions**:
   - Added a clear `pip install` command for users to install your package.

3. **Quick Start**:
   - Provided a simple example to help users get started quickly.

4. **Basic Usage**:
   - Added detailed examples for routing, dynamic routes, template rendering, static files, JSON responses, and middleware.

5. **Testing**:
   - Added instructions for running tests using `pytest`.
   - Included an example test file (`test_app.py`) to demonstrate how to test the framework.

6. **Contributing**:
   - Added guidelines for contributing to the project.

7. **License and Acknowledgments**:
   - Added a license section and acknowledged the inspiration behind the project.

---

### **How to Update Your `README.md`**
1. Copy the updated `README.md` content above.
2. Replace the existing `README.md` file in your repository with the new content.
3. Commit and push the changes:
   ```bash
   git add README.md
   git commit -m "Update README.md with improved documentation"
   git push origin main
   ```

---

### **Final Notes**
- The updated `README.md` is now more professional, user-friendly, and comprehensive.
- It includes all the necessary information for users to understand, install, and use your project.
- If you need further assistance, let me know! 😊
