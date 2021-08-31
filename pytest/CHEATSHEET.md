# Pytest Cheat Sheet
This is a cheat sheet of using pytest

# Usage
## test_sample.py
Run all functions in a file with:
```
pytest test_sample.py
```

## Classes
### Run eentire file:
```
pytest test_classes.py
```
### Run single test inside of a Class
Run a specific function inside a class:
```
pytest <file-name>.py::<class-name>::<function-name>
```
For example:
```
pytest test_classes.py::TestClass::test_two
```