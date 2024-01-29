© Danilo Florentino Maia, 2024

# IDP API Readme

## Overview

The Intelligent Diacritic Placer API (IDP API) is a Python and Flask—based application designed to convert Standard English (SE) texts into English with Diacritics (EwD). This API serves as a tool for linguistic research and educational purposes, particularly in the context of the PI Project.

## Features

- Converts SE text to EwD format.
- Supports different English accents for phonetic conversion.
- Utilizes a unique phonetic-to-graphemic conversion process.

## Installation

1. Clone the repository.
2. Install required dependencies: `pip install -r requirements.txt`.

## Usage

Start the API with `python app.py`. The API provides two main endpoints:

1. `/api/v1/get-phonetized-text`: Accepts SE text and an English accent, returning the phonetized version.
2. `/api/v1/convert-en-to-ewd`: Converts SE text to EwD, considering the specified English accent.

## Endpoints

### GET Phonetized Text

- **URL:** `/api/v1/get-phonetized-text`
- **Method:** `POST`
- **Body Parameters:**
  - `text`: SE text to be phonetized.
  - `accent`: English accent for phonetic conversion (default is `en-us`).

### Convert EN to EwD

- **URL:** `/api/v1/convert-en-to-ewd`
- **Method:** `POST`
- **Body Parameters:**
  - `text`: SE text to be converted to EwD.
  - `accent`: English accent for conversion (default is `en-us`).

## Documentation

Swagger documentation is available at `/swagger` for detailed endpoint usage.

## Testing

Unit tests are provided for various components. Run tests using `pytest`.

## Architecture

The IDP API is built as a monolithic architecture with a focus on simplicity and ease of deployment. It uses SQLite for lightweight data management and Flask for the web framework.

## Development and Deployment

- **TDD Approach:** Ensures quality and minimizes bugs.
- **CI/CD:** Simplified setup using GitHub Actions.
- **Monitoring and Logging:** Basic monitoring with Grafana and internal Flask logging.

## Security

- **Authentication:** Simplified OAuth 2.0 implementation.
- **Data Security:** Basic TLS for data transmission.

## Contributions

As this is a private project currently under development for the PI Project research, contributions are limited to authorized team members only. For involvement or collaboration inquiries, please send an email message to [contact@thepimethod.org](mailto:contact@thepimethod.org).

## Contact

For inquiries or assistance, get in touch with [contact@thepimethod.org](mailto:contact@thepimethod.org).

## License

This project is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit [http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/) or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

---

© Danilo Florentino Maia, 2024
