# Macondo Management

A CLI café order management system built in Python.

## Features

- Add orders from a predefined menu
- Show all orders with numbering
- Remove orders by number
- Checkout (calculates total and clears orders)
- Persistent storage with JSON
- Tested with pytest

## Requirements

- Python 3.13+
- pytest (for testing)

## Installation

1. Clone the repository:
   git clone https://github.com/Pmshrr/macondo-management.git
   cd macondo-management

2. Create a virtual environment:
   python -m venv .venv
   .venv\Scripts\Activate.ps1    # On Windows
   source .venv/bin/activate      # On macOS/Linux

3. Install dependencies:
   pip install -r requirements.txt

## Usage

Run the application:
python main.py

Then follow the menu:
1. Add order
2. Show orders
3. Remove order
4. Checkout
0. Exit

## Project Structure

- main.py         — CLI interface
- sales.py        — Business logic (orders, menu)
- test_sales.py   — Tests for sales.py

## Testing

Run tests:
pytest

## Technologies

- Python 3.13
- JSON (data storage)
- pytest (testing)
- Git (version control)

## Author

Parsa Mokri ([@Pmshrr](https://github.com/Pmshrr))
