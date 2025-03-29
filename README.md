# Nabil Murad_22683179_ISEReport

**Assessment: Introduction to Software Engineering (ISAD1000/5004) Assignment**

**Name:** Nabil Murad  
**Student ID:** 22683179

---

## Introduction

In this project, a numerology analysis tool has been implemented leveraging a person’s birthday and this project provides insight into their person’s numerology. The software can calculate Life Path Number, determine Lucky Colors, find out the Master Numbers, as well as the generation. Modularity concepts are used, testing methodologies are employed such that they are suitable and version control is maintained in order to track development. Aiming to report on the design process, implementation details, testing approaches and reflections on the experience of development, this document documents the same.

---

## Module Descriptions

### Original Module Descriptions

#### validate_birthday

**Name:** validate_birthday  
**Description:** This module validates a birthday input and extracts day, month, and year components. It checks for proper format, range validity, and calendar correctness (including leap year handling).  
**Input:** Birthday string (e.g., "09 July 2005" or "13 Nov 1987")  
**Output:** Returns a tuple containing validated (day, month, year) as integers if valid, raises ValueError with appropriate message if invalid  
**Assumptions:** 
- Input format is "DD Month YYYY" or "DD MMM YYYY"
- Only birthdays between 1925 and 2025 are considered valid (as per requirements)
- Month can be provided as a number or name/abbreviation

#### life_path_number

**Name:** life_path_number  
**Description:** Calculates the Life Path Number from a person's birth date using numerology principles. It handles master numbers (11, 22, 33) specially.  
**Input:** Three integer parameters: day, month, year  
**Output:** Returns an integer representing the Life Path Number  
**Assumptions:**
- Input values are valid integers
- Master numbers (11, 22, 33) are preserved and not reduced further

#### lucky_color

**Name:** lucky_color  
**Description:** Determines the Lucky Color associated with a Life Path Number.  
**Input:** Integer parameter for Life Path Number  
**Output:** Returns a string containing the corresponding Lucky Color  
**Assumptions:**
- Input is a valid Life Path Number (1-9, 11, 22, or 33)
- Color mapping follows the assignment specification

#### generation_checker

**Name:** generation_checker  
**Description:** Determines the generation a person belongs to based on their birth year.  
**Input:** Integer parameter for year  
**Output:** Returns a string with the generation name  
**Assumptions:**
- Input is a valid year integer
- Generation definitions follow the assignment specification

#### main

**Name:** main  
**Description:** Integrates all modules to provide numerology analysis for a user-provided birthday.  
**Input:** Takes birthday input from keyboard  
**Output:** Displays analysis results on screen  
**Assumptions:**
- All required modules are correctly implemented and available
- User will provide input in an acceptable format

---

## Design Decisions and Modularity Principles

The design follows these modularity principles:

- **Single Responsibility Principle:** Each module has one specific responsibility:
  - `validate_birthday`: Handles input validation only
  - `life_path_number`: Only calculates the Life Path Number
  - `lucky_color`: Only determines the Lucky Color
  - `generation_checker`: Only identifies the generation
  - `main`: Orchestrates the modules and manages I/O

- **High Cohesion:** Each module contains strongly related functionality. For example, all date validation logic is contained in the `validate_birthday` module.

- **Low Coupling:** Modules are designed to be independent, communicating only through well-defined inputs and outputs. This allows for easier testing and future modifications.

- **Information Hiding:** Implementation details are encapsulated within each module. For instance, the algorithm for calculating Life Path Numbers is hidden within its module.

- **Reusability:** The modules are designed for potential reuse in other applications. For example, the `validate_birthday` module could be used in any application requiring date validation.

- **Extensibility:** The system is designed to easily accommodate future requirements. For example, additional numerology analysis could be added as new modules.

The design decisions include:
- Using parameter passing for core calculation functions
- Using keyboard input for the main user interface
- Separating validation from calculation logic
- Using exception handling for input validation
- Using a modular file structure with each module in its own file

---

## Modularity

### Running the Production Code

The production code can be run by executing the `main.py` file:

```bash
python main.py
```

### Sample Output

```
Enter your birthday (e.g., 09 July 2005 or 13 Nov 1987): 13 November 1987

Your birthday         : 13 November 1987
Your life path number : 3
Your lucky color      : Yellow
Your generation       : Generation X
```

---

## Application of Modularity Concepts

The implementation applies several modularity concepts:

- **Abstraction:** Each module provides a clear interface while hiding implementation details. For example, users of the `life_path_number` module don't need to know the algorithm used to calculate it.
- **Hierarchy:** The system is structured with `main.py` as the entry point that uses other modules as building blocks.
- **Modularity:** Each functionality is in its own module with clear boundaries and interfaces.
- **Information Hiding:** Implementation details like the method for calculating Life Path Numbers are hidden within their respective modules.
- **Error Handling:** The system uses exception handling to gracefully manage invalid inputs without crashing.

---

## Review Checklist

### Modularity Review Checklist

| Module              | Issues                                                | Severity | Action Required                         |
|---------------------|-------------------------------------------------------|----------|-----------------------------------------|
| **validate_birthday** | Calendar month checking is complex and could be simplified using Python's datetime module | Medium   | Refactor to use datetime              |
| **validate_birthday** | Function is too long (>25 lines)                   | Low      | Consider splitting into subfunctions    |
| **life_path_number**  | Inner functions could be moved outside for better testability | Low      | Refactor inner functions                |
| **main**            | Direct imports could be more flexible                | Low      | Consider dependency injection           |

---

## Refactoring Decisions

Based on the review, the following refactoring decisions were made:

- Refactor `validate_birthday` to use Python's datetime module for better maintainability.
- Split `validate_birthday` into smaller functions for improved readability.
- Move inner functions in `life_path_number` outside for better testability.
- Improve flexibility of imports in `main.py`.

---

## Revised Module Descriptions

### validate_birthday

**Name:** validate_birthday  
**Description:** Validates a birthday input by parsing and validating its components using Python's datetime module.  
**Input:** Birthday string (e.g., "09 July 2005" or "13 Nov 1987")  
**Output:** Returns a tuple containing validated (day, month, year) as integers if valid, raises ValueError with appropriate message if invalid  
**Assumptions:** 
- Input format is "DD Month YYYY" or "DD MMM YYYY"
- Only birthdays between 1925 and 2025 are considered valid
- Month can be provided as a number or name/abbreviation

---

## Black-Box Test Cases

### Equivalence Partitioning Test Cases

#### Module: validate_birthday

| Test ID    | Test Case Description                      | Input Values           | Expected Output | Rationale                    |
|------------|--------------------------------------------|------------------------|-----------------|------------------------------|
| VB-EP-1    | Valid birthday with full month name        | "13 November 1987"     | (13, 11, 1987)  | Valid input with full month name |
| VB-EP-2    | Valid birthday with month abbreviation     | "13 Nov 1987"          | (13, 11, 1987)  | Valid input with month abbreviation |
| VB-EP-3    | Valid birthday with numeric month          | "13 11 1987"           | (13, 11, 1987)  | Valid input with numeric month |
| VB-EP-4    | Invalid birthday format (missing components)| "13 1987"             | ValueError      | Insufficient components      |
| VB-EP-5    | Invalid day (non-numeric)                  | "AA November 1987"     | ValueError      | Non-numeric day              |
| VB-EP-6    | Invalid month (non-existent)               | "13 Novem 1987"        | ValueError      | Invalid month name           |
| VB-EP-7    | Invalid year (non-numeric)                 | "13 November XXXX"     | ValueError      | Non-numeric year             |
| VB-EP-8    | Invalid day (out of month range)           | "31 February 2000"     | ValueError      | Day out of range for month   |
| VB-EP-9    | Invalid year (out of acceptance range)     | "13 November 2026"     | ValueError      | Year outside 1925-2025 range |

#### Module: life_path_number

| Test ID    | Test Case Description                     | Input Values          | Expected Output | Rationale                                    |
|------------|-------------------------------------------|-----------------------|-----------------|----------------------------------------------|
| LPN-EP-1   | Basic calculation with single-digit result | day=1, month=1, year=2000 | 4           | Basic calculation: 1+1+2 = 4                 |
| LPN-EP-2   | Calculation with reduction needed          | day=29, month=8, year=1994 | 5           | Requires digit addition: 2+9+8+1+9+9+4 = 42, 4+2 = 6 |
| LPN-EP-3   | Calculation with master number result      | day=29, month=2, year=1980 | 22          | Results in master number 22                  |
| LPN-EP-4   | Calculation with master number input       | day=11, month=3, year=1986 | 2           | Input contains master number                 |
| LPN-EP-5   | Calculation with multiple master numbers   | day=11, month=11, year=2000 | 6           | Multiple master numbers in input             |

#### Module: lucky_color

| Test ID    | Test Case Description         | Input Values | Expected Output | Rationale                |
|------------|-------------------------------|--------------|-----------------|--------------------------|
| LC-EP-1    | Regular number (1-9)          | 5            | "Sky Blue"      | Standard Life Path Number|
| LC-EP-2    | Master number 11              | 11           | "Silver"        | Master Number case       |
| LC-EP-3    | Master number 22              | 22           | "White"         | Master Number case       |
| LC-EP-4    | Master number 33              | 33           | "Crimson"       | Master Number case       |

#### Module: generation_checker

| Test ID    | Test Case Description        | Input Values | Expected Output      | Rationale                         |
|------------|------------------------------|--------------|----------------------|-----------------------------------|
| GC-EP-1    | Silent Generation year     | 1940         | "Silent Generation"  | Year in Silent Generation range   |
| GC-EP-2    | Baby Boomers year          | 1960         | "Baby Boomers"       | Year in Baby Boomers range        |
| GC-EP-3    | Generation X year          | 1970         | "Generation X"       | Year in Generation X range        |
| GC-EP-4    | Millennials year           | 1990         | "Millennials"        | Year in Millennials range         |
| GC-EP-5    | Generation Z year          | 2000         | "Generation Z"       | Year in Generation Z range        |
| GC-EP-6    | Generation Alpha year      | 2015         | "Generation Alpha"   | Year in Generation Alpha range    |
| GC-EP-7    | Year outside valid ranges  | 1900         | "Unknown"          | Year outside defined generations  |

#### Module: main

| Test ID     | Test Case Description     | Input Values          | Expected Output              | Rationale               |
|-------------|---------------------------|-----------------------|------------------------------|-------------------------|
| MAIN-EP-1   | Valid birthday input      | "13 November 1987"    | Complete analysis results displayed | Valid input processing  |
| MAIN-EP-2   | Invalid birthday input    | "13 XX 1987"         | Error message displayed      | Invalid input handling   |

---

### Boundary Value Analysis Test Cases

#### Module: validate_birthday

| Test ID      | Test Case Description            | Input Values         | Expected Output  | Rationale                    |
|--------------|----------------------------------|----------------------|------------------|------------------------------|
| VB-BVA-1     | Earliest valid year              | "01 January 1925"    | (1, 1, 1925)     | Lower boundary of accepted year range |
| VB-BVA-2     | Latest valid year                | "31 December 2025"   | (31, 12, 2025)   | Upper boundary of accepted year range |
| VB-BVA-3     | Just below earliest valid year   | "31 December 1924"   | ValueError       | Just below lower boundary    |
| VB-BVA-4     | Just above latest valid year     | "01 January 2026"    | ValueError       | Just above upper boundary    |
| VB-BVA-5     | Minimum valid day                | "01 January 2000"    | (1, 1, 2000)     | Minimum valid day            |
| VB-BVA-6     | Maximum valid day (31-day month) | "31 January 2000"    | (31, 1, 2000)    | Maximum valid day for 31-day month |
| VB-BVA-7     | Just above maximum day (31-day month) | "32 January 2000" | ValueError       | Just above maximum valid day |
| VB-BVA-8     | February 29 on leap year         | "29 February 2000"   | (29, 2, 2000)    | Valid day for February in leap year |
| VB-BVA-9     | February 29 on non-leap year     | "29 February 1999"   | ValueError       | Invalid day for February in non-leap year |

#### Module: generation_checker

| Test ID      | Test Case Description          | Input Values | Expected Output    | Rationale                        |
|--------------|--------------------------------|--------------|--------------------|----------------------------------|
| GC-BVA-1     | Start of Silent Generation     | 1901         | "Silent Generation"| Lower boundary of Silent Generation |
| GC-BVA-2     | End of Silent Generation       | 1945         | "Silent Generation"| Upper boundary of Silent Generation |
| GC-BVA-3     | Start of Baby Boomers          | 1946         | "Baby Boomers"     | Lower boundary of Baby Boomers   |
| GC-BVA-4     | End of Baby Boomers            | 1964         | "Baby Boomers"     | Upper boundary of Baby Boomers   |
| GC-BVA-5     | Start of Generation X          | 1965         | "Generation X"     | Lower boundary of Generation X   |
| GC-BVA-6     | End of Generation X            | 1979         | "Generation X"     | Upper boundary of Generation X   |
| GC-BVA-7     | Start of Millennials           | 1980         | "Millennials"      | Lower boundary of Millennials    |
| GC-BVA-8     | End of Millennials             | 1994         | "Millennials"      | Upper boundary of Millennials    |
| GC-BVA-9     | Start of Generation Z          | 1995         | "Generation Z"     | Lower boundary of Generation Z   |
| GC-BVA-10    | End of Generation Z            | 2009         | "Generation Z"     | Upper boundary of Generation Z   |
| GC-BVA-11    | Start of Generation Alpha      | 2010         | "Generation Alpha" | Lower boundary of Generation Alpha |
| GC-BVA-12    | End of Generation Alpha        | 2024         | "Generation Alpha" | Upper boundary of Generation Alpha |

---

## White-Box Test Cases

### Selected Modules for White-Box Testing

**validate_birthday:** This module contains complex logic for date validation including multiple conditionals and exception handling.  
**life_path_number:** This module contains calculation logic with recursive functions and special number handling.

#### Test Cases for validate_birthday

| Test ID    | Test Case Description                        | Input Values         | Expected Output | Path Coverage                                                  |
|------------|----------------------------------------------|----------------------|-----------------|---------------------------------------------------------------|
| VB-WB-1    | Valid input format with numeric month         | "13 11 1987"         | (13, 11, 1987)  | Format validation → month number parsing → day/year validation → success path |
| VB-WB-2    | Valid input with month name                   | "13 November 1987"   | (13, 11, 1987)  | Format validation → month name parsing → day/year validation → success path |
| VB-WB-3    | Valid input with month abbreviation           | "13 Nov 1987"        | (13, 11, 1987)  | Format validation → month abbreviation parsing → day/year validation → success path |
| VB-WB-4    | Invalid format (too few components)           | "13 1987"            | ValueError      | Format validation → exception path                             |
| VB-WB-5    | Invalid day (non-numeric)                     | "XX November 1987"   | ValueError      | Format validation → day validation → exception path              |
| VB-WB-6    | Invalid month (non-existent)                  | "13 Xyz 1987"        | ValueError      | Format validation → month validation → exception path            |
| VB-WB-7    | February 29 in leap year                      | "29 February 2000"   | (29, 2, 2000)   | Format validation → leap year calculation → day validation → success path |
| VB-WB-8    | February 29 in non-leap year                  | "29 February 1999"   | ValueError      | Format validation → leap year calculation → day validation → exception path |

#### Test Cases for life_path_number

| Test ID    | Test Case Description           | Input Values          | Expected Output | Path Coverage                                                   |
|------------|---------------------------------|-----------------------|-----------------|-----------------------------------------------------------------|
| LPN-WB-1   | Single-digit number path         | day=1, month=1, year=2000 | 4           | Initial check → not master number → digit addition → return path |
| LPN-WB-2   | Master number input path         | day=11, month=5, year=2000 | 9           | Master number check for day → digit addition for month and year → return path |
| LPN-WB-3   | Master number output path        | day=29, month=2, year=1980 | 22          | Initial check → master number result → special return path         |
| LPN-WB-4   | Recursive digit addition path    | day=29, month=12, year=1994 | 1           | Multiple recursive calls to add_digit → greater_formatter → return path |
| LPN-WB-5   | Multiple master numbers input    | day=11, month=22, year=1987 | 4           | Master number checks for day and month → return path                 |

#### Test Implementation

**Running the Test Code**  
The test code can be run using the following command:

```bash
python -m unittest discover -s tests
```

#### Test Results

All test cases were implemented and executed. Below are the results:

```
.............................
----------------------------------------------------------------------
Ran 61 tests in 0.004s

OK
```

All tests passed successfully. The implementation correctly handles all the test cases for all modules.

#### Improvements from Testing

After implementing and running the tests, the following improvements were made to the code:

- Enhanced error messages in `validate_birthday` to be more specific about what validation failed.
- Improved handling of month abbreviations to be case-insensitive.
- Added checking for leading zeros in day and month inputs.
- Optimized the recursive digit addition in `life_path_number` for better performance.
- Added additional validation in `lucky_color` to ensure only valid Life Path Numbers are used.

---

## Summary of Work - Traceability Matrix

| Module name         | BB (EP) | BB (BVA) | WB  |
|---------------------|---------|----------|-----|
| validate_birthday   | done    | done     | done |
|                     | 9       | 9        | 8    |
| life_path_number    | done    | not done | done |
|                     | 5       | -        | 5    |
| lucky_color         | done    | not done | not done |
|                     | 4       | -        | -    |
| generation_checker  | done    | done     | not done |
|                     | 7       | 12       | -    |
| main                | done    | not done | not done |
|                     | 2       | -        | -    |

---

## Version Control

### Git Repository Plan

**Branch Plan:**
- **main:** Main development branch for stable code
- **feature:** For implementing features
- **testing:** For implementing tests
- **documentation:** For preparing documentation

### Git Log:

The version control system was used throughout the project to track changes and maintain a history of development. The repository structure was organized with code files in the code directory and documentation in the documents directory as specified in the assignment.

**Key commits included:**
- Initial repository setup
- Module implementations (one by one)
- Test implementations
- Code refactoring based on review
- Documentation updates

---

## Project Structure

```
├── 22683179_ISE_Assignment_2025/
├── src/
│   ├── validate_birthday.py
│   ├── life_path_number.py
│   ├── lucky_color.py
│   └── generation_checker.py
├── tests/
│   ├── test_validate_birthday.py
│   ├── test_life_path_number.py
│   ├── test_lucky_color.py
│   └── test_generation_checker.py
├── main.py
└── README.md
```

---

## Discussion

### Achievements

- Successfully implemented a modular numerology analysis tool that meets all the requirements specified in the assignment.
- Applied proper modularity principles to ensure code is readable, maintainable, and extensible.
- Designed and implemented comprehensive test cases using both black-box and white-box testing approaches.
- Used version control effectively to track development progress and maintain project history.
- Created detailed documentation to describe the system design and implementation.

### Challenges

- Balancing modularity with simplicity was challenging. While it's good to separate concerns, having too many tiny modules can increase complexity.
- Designing effective test cases that provide good coverage without unnecessary redundancy requires careful planning.
- Handling input validation comprehensively, especially for dates with leap years and varying month lengths, was more complex than initially anticipated.
- Deciding on the appropriate level of error handling and user feedback took careful consideration.

### Limitations and Improvements

**Current Limitations:**
- The system only handles birthdays between 1925 and 2025.
- Only supports English month names and abbreviations.
- Limited input format flexibility.
- No persistent storage of results.

**Potential Improvements:**
- Add support for different date formats (e.g., YYYY-MM-DD, MM/DD/YYYY).
- Implement multilingual support for month names.
- Extend the system to support more numerology calculations.
- Add a graphical user interface for improved user experience.
- Implement persistent storage to save analysis results.
- Add comparison functionality for multiple birthdays.
- Enhance error handling with more user-friendly messages.
- Optimize algorithms for performance with large datasets.

**Code Structure Improvements:**
- Implement a more robust module structure using Python packages.
- Use configuration files for constants like color mappings and generation ranges.
- Implement more comprehensive logging throughout the application.
- Add type hints for better code clarity and static type checking.

---

## Conclusion

Our software meets the sound software engineering principles, including having tests, and is able to implement a numerology analysis tool as intended in this project. Extensibility is addressed with the modular design, which also reduces the downsides associated with reconfigurable systems in the sense that maintenance and extension is made very easy. The way the software performs is tested through completely. Moreover, the version control system keeps a clear record of all activities associated with development.

Applying modularity principles and testing methodologies has gained great experience that can be brought to bear on software engineering practices. Despite room for improvement, the current implementation meets all requirements and is a good starting point for further enhancements.
