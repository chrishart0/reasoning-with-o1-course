# Notes from [Reasoning with o1 DeepLearning.ai course](https://learn.deeplearning.ai/courses/reasoning-with-o1/lesson/1/introduction)

## Instructions

Follow these steps to set up the project:

1. **Set up Python version with pyenv:**
   *Install pyenv if you don't have it: <https://github.com/pyenv/pyenv>*

   ```sh
   # Install specific Python version
   pyenv install 3.12
   ```

2. **Create a virtual environment:**
   ```sh
   python -m venv .venv
   ```

3. **Activate the virtual environment:**
   - On macOS and Linux:
     ```sh
     source .venv/bin/activate
     ```
   - On Windows:
     ```sh
     .venv\Scripts\activate
     ```

4. **Install dependencies with Poetry:**
   Check if you have poetry by running `poetry --version`

   If you don't have poetry, go install it: <https://python-poetry.org/docs/>

   ```sh
   poetry install
   ```

5. **Setup your .env**
Copy the `.env.example` file to `.env` and update the values:


6. **Optional: Setup pre-commit hook**
```bash
pre-commit install
```

## Run the openai usage examples

Simple gpt-4o chat
```bash
```

Simple OpenAI o1-mini call
```bash
python template_python_fastapi_repo/examples/simple-o1-api-call.py
```

## Running the FastAPI server

To run the FastAPI server, use the following command:
```sh
uvicorn template_python_fastapi_repo.main:app --reload
```

Now navigate to <http://127.0.0.1:8000/docs> and you will see the running FastAPI OpenAI spec

## Testing

This project includes code coverage requirements to ensure the quality of the code. To measure code coverage, we use `pytest-cov`.

### Running Tests with Code Coverage

To run the tests and measure code coverage, use the following command:
```sh
poetry run pytest --cov --cov-report=term-missing
```

## Linting

```bash
poetry run black .
poetry run flake8 .
```

## Environment Variables

This project uses environment variables to manage sensitive information and configuration settings. Follow these steps to set up and use the environment variables:

1. **Create a `.env` file:**
   Create a `.env` file in the root of the repository with the following content:
   ```sh
   OPENAI_API_KEY=sk-proj-...
   ```

2. **Run the needed services:**
   ```sh
   docker-compose up -d
   ```

2. **Run the FastAPI server:**
   Use the following command to run the FastAPI server:
   ```sh
   uvicorn template_python_fastapi_repo.main:app --reload
   ```
3. **Verify the settings:**
   Ensure that the environment variables are loaded correctly by checking the output of the FastAPI server or running the tests.

## Basic Pydantic Model

This project includes a basic Pydantic model to validate and serialize data.

### HelloWorld Model

The `HelloWorld` model has the following field:
- `message`: a string representing the message

### Example Usage

Here's an example of how to create a `HelloWorld` instance and print it:

```python
from pydantic import BaseModel

class HelloWorld(BaseModel):
    message: str

def create_hello_world(message: str) -> HelloWorld:
    hello_world = HelloWorld(message=message)
    print(hello_world)
    return hello_world

# Example usage
create_hello_world("Hello, World!")
```

## Updating Your Repository

If you have created a repository from this template and want to update it with the latest changes from the template, follow these steps:

1. **Add the template repository as a remote:**
   ```sh
   git remote add template https://github.com/chrishart0/template-python-fastapi-repo.git
   ```

2. **Fetch the latest changes from the template:**
   ```sh
   git fetch template
   ```

3. **Merge the changes into your main branch:**
   ```sh
   git checkout main
   git merge template/main
   ```

4. **Resolve any merge conflicts:**
   If there are any merge conflicts, resolve them in your code editor and commit the changes.

5. **Push the updates to your repository:**
   ```sh
   git push origin main
   ```

By following these steps, you can keep your project up-to-date with the latest improvements and features from the template repository.

# ToDo:

- Maybe add a UI