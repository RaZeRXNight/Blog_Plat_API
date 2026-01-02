# Blog-api
Blog-api is a restful backend api project written in python that handles the CRUD operations of a Blog Platform.  The Blogs are stored within a sql database

This project should not be used in a production environment.
## Features
This project is the backend of a Blog Platform, 
- Handles the Creation, Reading, Updating and Deleting of Blog Posts.
- Completes SQL Operations for storing items.

## How to use
Prerequisites:
- Python 3.8+
- Either the project's "uv" project manager (use `uv sync`) or pip for installing dependencies.

1. Create a `.env` file in the project root with at least:
```
APP_NAME=Blog-api
HOST=127.0.0.1
PORT=5000
```

2. Install dependencies:
- With uv: `uv sync`
- Or with pip: `pip install Flask python-dotenv`

3. Start the application:
```
python app.py
```
The app will create `app/Blog.db` on first run if it doesn't exist.



## How to Install
The project uses uv project manager to handle its dependencies.  Use `uv sync` to download the dependencies for the app.

Dependencies
- Flask
- dotenv

## References
- https://roadmap.sh/projects/blogging-platform-api