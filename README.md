<div align="center">
  <br>
  <img alt="Open Sauced" src="https://cdn.discordapp.com/attachments/980268278284976189/1093756002282766436/PNG-brasa-logo_1.png" width="300px">
  <h1> 🇧🇷 BRASA API 🇧🇷</h1>
  <strong>🧑‍💻 UCF BRASA's student created API 🧑‍💻 </strong>
</div>

## 📖 Prerequisites

### Tools/Technologies (required)
- [Python@3.11](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)
- [MongoDBCompass](https://www.mongodb.com/try/download/compass) or [MongoDB VSC Extension](https://marketplace.visualstudio.com/items?itemName=mongodb.mongodb-vscode)

### VSC Extensions (recommended)
- [Black](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
- [Flake8](https://marketplace.visualstudio.com/items?itemName=ms-python.flake8)
- [isort](https://marketplace.visualstudio.com/items?itemName=ms-python.isort)
- [Python Indent](https://marketplace.visualstudio.com/items?itemName=KevinRose.vsc-python-indent) 
- [BetterTOML](https://marketplace.visualstudio.com/items?itemName=bungcip.better-toml)
- [ENV](https://marketplace.visualstudio.com/items?itemName=IronGeek.vscode-env)

### Environment Variables file (required)
Before running the app, you need to fill out the `.env` file. Please reach out to either:
  - [Fachetti (EniGzz#0011)](https://discordapp.com/users/294195589820710912)
  - [Duda (Joazeiro#0815)](https://discordapp.com/users/401588155788296194)


## 🖥️ Local development
### Installing
Run the following command to install all the project dependencies.

```shell
poetry install
```

```shell
poetry run pre-commit install
```

### Running
```shell
poetry run start
```
The application will be available at [https://localhost:8080](http://localhost:8080)


## 📓 Documentation
### Swagger Docs
> https://brasa-api.up.railway.app/docs

### Redoc Docs
> https://brasa-api.up.railway.app/redoc


## 🧪 Test

For running the unit test suite, use the following command: 

```shell
poetry run pytest
```

## 🧰 Built With

  - [FastAPI](https://fastapi.tiangolo.com/) - The API framework used
  - [MongoDB](https://www.mongodb.com) - NoSQL database
  - [Beanie](https://beanie-odm.dev) - Database ODM (Object Document Mapper)
  - [Poetry](https://python-poetry.org) - Dependency and virtual environment manager
  - [Flake8](https://flake8.pycqa.org/en/latest/) - Code Linter
  - [Black](https://black.readthedocs.io/en/stable/) - Code Formatter

## Deployment

We are using [Railway🚅](https://railway.app) to deploy our app using `uvicorn`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
