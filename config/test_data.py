"""
Test data parameters for test scenarios.
"""

# User data
USER_DATA = {
    'default_user': {
        'username': 'testuser',
        'password': 'password123',
        'email': 'testuser@example.com',
        'age': 25,
    },
    'minor_user': {
        'username': 'minoruser',
        'password': 'password123',
        'email': 'minor@example.com',
        'age': 15,  # Example of the age parameter you mentioned
    },
    'senior_user': {
        'username': 'senioruser',
        'password': 'password123',
        'email': 'senior@example.com',
        'age': 65,
    }
}

# Product data
PRODUCT_DATA = {
    'product1': {
        'name': 'Test Product 1',
        'price': 19.99,
        'quantity': 1,
    },
    'product2': {
        'name': 'Test Product 2',
        'price': 29.99,
        'quantity': 2,
    }
}

# Form data
FORM_DATA = {
    'registration': {
        'first_name': 'John',
        'last_name': 'Doe',
        'phone': '1234567890',
        'address': '123 Test Street',
        'city': 'Test City',
        'zip_code': '12345',
        'country': 'Test Country',
    }
}

# Test scenarios
SCENARIOS = {
    'login_success': {
        'description': 'Successful login with valid credentials',
        'expected_result': 'User should be logged in and redirected to dashboard',
    },
    'login_failure': {
        'description': 'Failed login with invalid credentials',
        'expected_result': 'Error message should be displayed',
    },
    'age_verification': {
        'description': 'Age verification for different user types',
        'expected_result': {
            'minor': 'Access denied to age-restricted content',
            'adult': 'Access granted to all content',
            'senior': 'Special discount applied',
        }
    }
}

# Environment specific data
ENVIRONMENTS = {
    'dev': {
        'url': 'https://dev.example.com',
        'api_key': 'dev_api_key',
    },
    'staging': {
        'url': 'https://staging.example.com',
        'api_key': 'staging_api_key',
    },
    'prod': {
        'url': 'https://example.com',
        'api_key': 'prod_api_key',
    }
}

def get_user_data(user_type='default_user'):
    """
    Get user data by user type
    """
    return USER_DATA.get(user_type, USER_DATA['default_user'])

def get_scenario_data(scenario_name):
    """
    Get scenario data by scenario name
    """
    return SCENARIOS.get(scenario_name, {})

def get_environment_data(env='dev'):
    """
    Get environment specific data
    """
    return ENVIRONMENTS.get(env, ENVIRONMENTS['dev'])
