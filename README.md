# Selenium BDD Testing Framework

A professional testing framework using Python with Selenium, pytest, and Behave for Behavior-Driven Development (BDD), following the Page Object Model (POM) principles.

## Project Structure

```
selenium-bdd-framework/
├── config/                  # Configuration files and test data
│   ├── config.py            # Configuration settings
│   └── test_data.py         # Test data parameters
├── drivers/                 # WebDriver executables
├── features/                # BDD feature files
│   ├── environment/         # Behave environment hooks
│   │   └── environment.py   # Behave environment setup
│   ├── steps/               # Step definitions
│   │   └── common_steps.py  # Common step implementations
│   └── example.feature      # Example feature file
├── page_objects/            # Page Object Model classes
│   ├── base_page.py         # Base page object class
│   └── example_page.py      # Example page object
├── reports/                 # Test reports and screenshots
├── utils/                   # Utility functions and helpers
│   ├── driver_factory.py    # WebDriver factory
│   └── helpers.py           # Helper functions
├── conftest.py              # pytest fixtures and configuration
├── pytest.ini               # pytest configuration
├── behave.ini               # behave configuration
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

## Setup

1. Install Python 3.8 or higher
2. Create and activate a virtual environment:
   ```
   # Create virtual environment
   python -m venv venv

   # Activate on Windows
   venv\Scripts\activate

   # Activate on macOS/Linux
   source venv/bin/activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Download appropriate WebDriver executables and place them in the `drivers` directory or use webdriver-manager

## Running Tests

### Using Behave:
```
# Make sure your virtual environment is activated
behave features/
```

### Using pytest:
```
# Make sure your virtual environment is activated
pytest
```

## Configuration

Test configuration and parameters are stored in the `config` directory. You can modify these files to adjust browser settings, test data, and other parameters.

## Reports

Test reports are generated in the `reports` directory. HTML reports are available after test execution.

## Adding New Tests

1. Create new feature files in the `features` directory
2. Implement step definitions in the `features/steps` directory
3. Create page objects in the `page_objects` directory
4. Add test data in the `config/test_data.py` file
