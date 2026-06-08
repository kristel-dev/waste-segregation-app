```markdown
# Waste Segregation App

## Description
The Waste Segregation App is a desktop-based tool developed in Python that helps users properly dispose of waste items by categorizing them into appropriate bins. The application uses the Strategy design pattern to support multiple input methods (console and GUI) and multiple output methods (screen display and GUI display). It helps users identify whether waste items should go to Recyclable, Organic, Hazardous, E-waste, or General waste bins.

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

Spelling-Corrector-Application/
- interfaces/
  - __init__.py
  - idata_service.py
  - ispell_service.py
- models/
  - __init__.py
  - word.py
- services/
  - __init__.py
  - spell_service.py
- tests/
  - __init__.py
  - test_spell_service.py
  - test_algorithms.py
  - test_processor.py
- app_gui.py
- main.py
- processor.py
- definitions.py
- dictionary.txt
- input_reader.py
- output_writer.py
- spell_checker_module.py
- README.md
- .gitignore


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
   ```

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
  GitHub: @renieldave

- Kristel Kate Guray
  GitHub: @kristel-dev

---

In Partial Fulfillment of the Requirements for the Subject CC103 Computer Programming 2  
Bachelor of Science in Information Technology at Sorsogon State University Bulan Campus.  
Under the supervision of Professor John Mark Gabrentina.
```
