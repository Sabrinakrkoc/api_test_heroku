**API Testing - Heroku Booker**  

This repository contains automated tests for the Heroku Booker API, covering authentication, creation, updating, deletion, and validation of bookings.  

# Project Structure:
/api_test_herokuapp
  /apitest
      /config           # Environment and log configurations
          settings.py   #  Loads environment variables
          logging_config.py  # Log configuration
      /test             # Test files organized by functionality
          test_create_booking.py
          test_delete_booking.py
          test_invalid_auth.py
          test_invalid_booking.py
          test_partial_update_booking.py
          test_retrieve_booking.py
          test_unauthorized_delete_booking.py
          test_unauthorized_update.py
          test_update_booking.py
          test_valid_auth.py
      /utils            # Reusable functions (requests, random data generation)
  /reports              # Execution reports (HTML, etc)
  .env                  # Environment variables (DO NOT upload to Git)
  pytest.ini            # Pytest configuration
  requirements.txt      # Project dependencies

 # Prerequisites
- Python 3.13+  
- Virtualenv  
- Dependencias instaladas (`requests`, `pytest`, etc.)  

# Installation 
- Clonar el repositorio:
git clone https://github.com/tuusuario/api_test_herokuapp.git
cd api_test_herokuapp

# Create virtual environment
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure Environment Variables
-Create a .env file at the root of the project with the required credentials:

BASE_URL=https://restful-booker.herokuapp.com
USERNAME=admin
PASSWORD=password123

🚀 Running Tests
# Run all tests:
pytest

# Generate HTML report:
pytest --html=reports/test_report.html

# Tested Features 

- Authentication (/auth)
- Booking creation (/booking) 
- Booking updates (PUT / PATCH)
- Booking deletion (DELETE)
- Tests with invalid data

##Continuous Improvement 
# Next steps:

-Implement load testing
-Add more edge case validations
-Integrate with CI/CD

