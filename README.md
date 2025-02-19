# Playfair Cipher Web Application

A modern web application implementing the classical Playfair cipher encryption technique with a user-friendly interface.

## Features

- 🔐 Encrypt and decrypt messages using the Playfair cipher algorithm
- 📊 Visual 5x5 key matrix display
- 🎨 Modern, responsive user interface
- ⚡ Real-time encryption/decryption
- 🔄 Input validation and error handling

## Technology Stack

- **Backend**: Python/Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Bootstrap 5, Font Awesome
- **Testing**: pytest

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Owusu1946/PlayFair_Cypher_Algorithm.git
```

2. create and activate virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python run.py
```

5. Open your browser and navigate to:

```bash
http://127.0.0.1:5000   
```


The application will be available at `http://localhost:5000`

## Usage

1. Enter a key in the key input field
2. Enter the text you want to encrypt/decrypt
3. Click either the "Encrypt" or "Decrypt" button
4. View the result and the generated key matrix

## How the Playfair Cipher Works

The Playfair cipher uses a 5x5 matrix of letters constructed using a keyword. The algorithm follows these rules:

1. The matrix is filled with the keyword first (excluding duplicates)
2. Remaining alphabet letters fill the matrix (I/J are combined)
3. Message is split into pairs of letters
4. Each pair is encrypted/decrypted based on their position in the matrix:
   - Same row: Use letters to the right (wrapping around)
   - Same column: Use letters below (wrapping around)
   - Different row/column: Use rectangle corners

## Project Structure

```plaintext
layfair-cipher/
├── app/
│ ├── static/
│ │ ├── css/
│ │ └── js/
│ ├── templates/
│ ├── init.py
│ ├── cipher.py
│ └── routes.py
├── config.py
├── requirements.txt
└── run.py
```


## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Implementation based on the classical Playfair cipher algorithm
- UI design inspired by modern web applications
- Built with Flask microframework