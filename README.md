# Number Classification API

# Overview:

The Number Classification API is a simple RESTful service that analyzes a given number and returns its mathematical properties, such as whether it is prime, perfect, or an Armstrong number. Additionally, it fetches a fun fact about the number.

# Features:

 * Check if a number is prime

 * Check if a number is perfect

 * Check if a number is an Armstrong number

 * Determine if a number is even or odd

 * Calculate the digit sum of the number

 * Retrieve a fun fact about the number

# SetUp Instructions:

1. Clone the repository
  * git clone https://github.com/brain188/Number-Classifier-API.git

2. Create a virtual environment
  * python -m venv venv
  * source venv/bin/activate  # macOS/Linux  
  * venv\Scripts\activate     # Windows

3. install Dependencies
  * pip install -r requirements.txt

4. Run the project locally
  * python wsgi.py


# API Endpoint:

1. Classify a Number

  * Endpoint: GET http://127.0.0.1:5000/api/classify-number?number=20

  * Parameters:

     * number (integer) - The number to classify.

2. Response: an exmaple

{
  "digit_sum": 2,
  "fun_fact": "20 is the number of ounces in Venti size coffees at Starbucks coffee shops.",
  "is_perfect": false,
  "is_prime": false,
  "number": 20,
  "properties": [
    "even"
  ]
}

# Technologies Used

  * Flask (Python web framework)

  * Unittest (Testing framework)

  * Render (Deployment)