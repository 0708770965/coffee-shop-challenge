# Coffee Shop Challenge

This project is a simple Python application modeling a coffee shop ordering system. It demonstrates basic object-oriented programming concepts including classes, type checking, and error handling.

## Project Structure

- `customer.py`: Defines the `Customer` class representing a customer.
- `coffee.py`: Defines the `Coffee` class representing a coffee type.
- `order.py`: Defines the `Order` class representing an order placed by a customer for a specific coffee at a given price.
- `debug.py`: A script to create sample customers, coffees, and orders, and print their details to verify correctness.
- `tests/`: Directory containing unit tests for the classes.

## Features

- Creation of customers and coffee types.
- Creation of orders linking customers and coffees with price validation.
- Type checking to ensure correct object types are used.
- Price validation to ensure prices are within a reasonable range (1.0 to 10.0).
- Error handling for invalid inputs.

## How to Run

1. Ensure you have Python 3 installed.
2. Run the `debug.py` script to see example usage and output:
   ```bash
   python3 debug.py
   ```
3. To run tests (if any), use your preferred test runner, for example:
   ```bash
   pytest tests/
   ```

## Error Cases

- Creating an order with invalid customer or coffee types will raise a `TypeError`.
- Creating an order with a price outside the range 1.0 to 10.0 will raise a `ValueError`.
- Creating a coffee with a name shorter than 2 characters will raise a `ValueError`.

## Notes

- The project is designed for educational purposes to demonstrate basic Python OOP and validation.
- The `debug.py` script includes commented-out lines to test error cases.

## Author

This project was created as part of a coding challenge.
