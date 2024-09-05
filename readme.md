© Danilo Florentino Maia, 2024

# IDP API Readme

## Overview

The **Intelligent Diacritic Placer API (IDP API)** is an experimental web application built with Python and Flask, designed to convert standard English (En) texts (without diacritics) into **English with Diacritics (EwD)**. This project is part of the **EwD Project**, aimed at providing a phonetic transcription tool for linguistic research, educational purposes, and easing the learning process of English pronunciation.

## Features

- **Convert En to EwD:** Efficiently transforms standard English text (En) into EwD format.
- **Accent support:** Handles various English accents for accurate phonetic transcription.
- **Phonetic-graphemic conversion:** Implements the EwD Grapheme-Phoneme Mapping, ensuring consistent phonetic representation in EwD.

## Installation

1. Clone the repository.
2. Install the required dependencies: `pip install -r requirements.txt`.

## Usage

To start the API, run:

```bash
python app.py
```

### Endpoints:

1. **Phonetize text:**

   - **URL:** `/api/v1/get-phonetized-text`
   - **Method:** `POST`
   - **Parameters:**
     - `text`: The En text to phonetize.
     - `accent`: The chosen English accent (default: `en-us`).

2. **Convert En to EwD:**
   - **URL:** `/api/v1/convert-en-to-ewd`
   - **Method:** `POST`
   - **Parameters:**
     - `text`: The En text to convert to EwD.
     - `accent`: The preferred English accent (default: `en-us`).

## Conversion Process

The process for converting En to EwD follows two key steps:
pytest

1. **Phonetic conversion:**
   The input En text is phonetically transcribed according to the specified accent using the `phonemizer` library.

2. **Graphemic mapping:**
   The phonetic transcription is then mapped to its corresponding EwD representation using the **EwD Grapheme-phoneme mapping**, which assigns diacritical marks to reflect pronunciation.

## Documentation

Detailed API usage documentation is available via **Swagger** at `/swagger`.

## Testing

Unit tests are provided for several components. Run the tests using the `pytest` command.

## Architecture

The IDP API is built as a monolithic architecture with a focus on simplicity and ease of deployment. It uses SQLite for lightweight data management and Flask as a web framework.

## Development and Deployment

- **Test-Driven Development (TDD):** Fosters quality code and reduces errors.
- **CI/CD:** Managed via GitHub Actions for streamlined development and deployment.
- **Monitoring:** Basic monitoring with Grafana and internal Flask logging.

## Security

- **Authentication:** Simplified implementation of OAuth 2.0.
- **Data security:** Basic TLS for data transmission.

## Expansion to Other Languages and Accents

### Expansion Possibilities

The IDP API, currently focused on converting standard English to English with Diacritics (EwD), was designed with an architecture that allows for expansion to other languages and a variety of accents. This expansion potential opens new fronts for linguistic research and educational applications in a global context.

### Support for Different Languages

The incorporation of new languages into the IDP API can be achieved by adapting the phonetic conversion process and the grapheme-to-phoneme mapping for each specific language. This includes integrating phonetic libraries and databases that support accurate phonetic transcription for those languages.

### Varied Accents

As is already done with English, the IDP API can be adapted to support different accents within the same language. This is essential for capturing the phonetic nuances that characterize regional or national accents, enriching the learning experience and enhancing the precision of linguistic research.

### Challenges and Considerations

Expanding to other languages and accents involves challenges such as the need for in-depth knowledge of the phonetic characteristics of each language and the availability of detailed phonetic and lexical resources. Additionally, it is crucial to consider cultural and linguistic particularities to ensure an accurate and respectful representation of the languages.

## Future of the IDP API

The future vision for the IDP API includes creating a robust and versatile platform that can serve as a valuable tool for education and linguistic research across diverse languages and accents, thereby promoting a broader and more inclusive understanding of the various forms of human expression around the world.

## Contributions

As this is a private project currently under development for the **EwD Project** research, contributions are limited to authorized people only. For inquiries about involvement or collaboration, please send an email to [contact@ewdproject.org](mailto:contact@ewdproject.org).

## Contact

For inquiries or assistance, please contact [contact@ewdproject.org](mailto:contact@ewdproject.org).

---

© Danilo Florentino Maia, 2024
