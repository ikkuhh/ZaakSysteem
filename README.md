# Zaaksysteem

Zaaksysteem is a small Python project for the backend test case.

## Getting started

Clone the repository:

```bash
$ git clone git@github.com:ikkuhh/Zaaksysteem.git
```

Enter the project root directory:

```bash
$ cd Zaaksysteem
```

The project expects a file `src/.env` with the following API config parameters:
```text
API_KEY=...
API_INTERFACE_ID=...
CASETYPE_ID=...
```

Create this file with the corresponding values before starting the server. See [python-decouple](https://pypi.org/project/python-decouple/#env-file) for more information about the `.env` file syntax.

## Usage Project

The project can be started using:
```bash
docker-compose up
```

A webserver will start on port `6543` with a single API endpoint `/`. The endpoint will process a CSV file and create a Zaaksysteem Case object for each row. Example usage:

```bash
curl localhost:6543 -H "Content-Type: text/csv" --data-binary "@file_name.csv"
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
