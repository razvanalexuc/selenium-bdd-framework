#!/bin/bash
echo "Setting up Selenium BDD Framework environment..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment already exists."
fi

# Activate virtual environment and install dependencies
echo "Activating virtual environment and installing dependencies..."
source venv/bin/activate
pip install -r requirements.txt

echo ""
echo "Setup complete! Virtual environment is activated."
echo "To run tests, use:"
echo "    behave features/"
echo "    or"
echo "    pytest"
echo ""
echo "To deactivate the virtual environment when done, type:"
echo "    deactivate"
echo ""
