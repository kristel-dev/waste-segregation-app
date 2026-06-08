# Waste Segregation App

## Description
The Waste Segregation App is a user-friendly application designed to help users identify, classify, and properly dispose of different types of waste materials. The system promotes environmental awareness by providing accurate waste categories, disposal guidelines, and segregation tips to encourage responsible waste management.

Users can search for a specific waste item, browse waste categories, or view all available waste materials in the database. The application automatically suggests matching items while typing, making it easier to find information quickly. Once an item or category is selected, the app displays proper disposal instructions and environmental reminders to guide users in handling waste responsibly.

This project aims to support sustainable practices, improve waste segregation knowledge, and contribute to cleaner communities through accessible and educational technology.

---

## Features

### Feature 1: Multiple Input Strategies
Allows users to enter waste items through different methods - console input or graphical user interface (GUI).

### Feature 2: Waste Categorization
Identifies and categorizes waste items into appropriate disposal categories (Recyclable, Organic, Hazardous, E-waste, General) based on predefined guidelines.

### Feature 3: Disposal Guidance
Provides proper disposal instructions and feedback for each waste item, helping users understand how to segregate waste correctly.

---

## Technologies Used

- Python 3.8+
- Tkinter (GUI Input/Output)
- Strategy Design Pattern
- Pytest (Unit Testing)

---

## OOP Concepts Implemented

- Encapsulation - Data hiding within waste item and disposal guide classes
- Polymorphism - Multiple input/output strategies implementing same interfaces
- Strategy Pattern - Dynamic selection of input/output methods at runtime
- Abstraction - Abstract base classes define strategy contracts
- Separation of Concerns - Clear separation between models, services, and strategies

---

## Project Structure

waste_segregation-app/
│
├── .gitignore                          # Git ignore file
├── .pytest_cache/                      # Pytest cache directory
├── CACHEDIR.TAG                        # Cache directory tag
├── README.md                           # Project documentation
├── main.py                             # Main entry point of the application
│
├── application/                        # Core application logic
│   ├── __pycache__/
│   ├── __init__.py
│   └── controller.py                   # Application controller
│
├── models/                             # Data model classes
│   ├── __pycache__/
│   ├── __init__.py
│   ├── disposal_guide.py               # Disposal guide model
│   ├── waste_category.py               # Waste category model
│   └── waste_item.py                   # Waste item model
│
├── repositories/                       # Data storage and retrieval
│   ├── __pycache__/
│   ├── __init__.py
│   └── waste_repository.py             # Repository for waste data
│
├── services/                           # Business logic layer
│   ├── __pycache__/
│   ├── __init__.py
│   └── waste_service.py                # Waste categorization service
│
├── strategies/                         # Strategy pattern implementations
│   ├── __pycache__/
│   ├── __init__.py
│   ├── input/                          # Input strategies (folder)
│   ├── output/                         # Output strategies (folder)
│   ├── output_strategy.py              # Output strategy interface/classes
│   └── screen_display.py               # Screen display output strategy
│
└── tests/                              # Unit tests
    ├── __pycache__/
    ├── __init__.py
    ├── test_models.py                  # Tests for models
    ├── test_repository.py              # Tests for repositories
    ├── test_service.py                 # Tests for services
    └── test_strategies.py              # Tests for strategies


```
## Installation

Prerequisites:
- Python 3.8 or higher
- pip (Python package manager)
- tkinter (usually comes with Python)

Steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/kristel-dev/waste-segregation-app.git
   cd waste-segregation-app

2. Navigate to the application folder:
   ```bash
   cd WASTE_SEGREGATION_APP
   ```

3. Run the application:
   ```bash
   python main.py
   ```

---

## Running the Application

Console Mode (Default):
   ```bash
   python main.py
   ```

The application will prompt you to choose input and output methods.

---

## Running the Tests

   ```bash
   pytest -v
   ```

---

## Sample Usage

Input:
   ```
   Enter waste item: plastic bottle
   Enter waste item: broken glass
   Enter waste item: banana peel
   Enter waste item: used battery
   ```

Output:
   ```
   Item: plastic bottle
   Category: Recyclable
   Disposal: Clean and place in recycling bin
   
   Item: broken glass
   Category: Recyclable
   Disposal: Wrap in paper before placing in recycling bin
   
   Item: banana peel
   Category: Organic
   Disposal: Place in compost bin
   
   Item: used battery
   Category: Hazardous
   Disposal: Dispose at designated hazardous waste collection point
   ```

---

## Design Patterns Implemented

- **Strategy Pattern** - Allows switching between different input (Console/GUI) and output (Screen/GUI Display) methods at runtime
- **Repository Pattern** - Manages waste item data storage and retrieval
- **Controller Pattern** - Coordinates between models, services, and strategies

---

## Sustainable Development Goal (SDG)

### SDG 11: Sustainable Cities and Communities
### SDG 12: Responsible Consumption and Production

This application supports SDG 11 and SDG 12 by promoting proper waste segregation and disposal practices. It educates users on correct waste management, reducing environmental pollution, and encouraging recycling and responsible consumption habits.

---

## Testing

The application was tested using:

- Functional Testing
- User Interface Testing (GUI)
- Manual Testing
- Error Handling Testing
- Automated Unit Testing using Pytest

All test cases passed successfully, confirming that the system functions correctly and reliably.

---

## Authors

- Reniel Dave Gordola
  GitHub: @gordolarenieldave-hash

- Kristel Kate Guray
  GitHub: @kristel-dev

---

In Partial Fulfillment of the Requirements for the Subject CC103 Computer Programming 2  
Bachelor of Science in Information Technology at Sorsogon State University Bulan Campus.  
Under the Supervision of Professor John Mark Gabrentina.
```
