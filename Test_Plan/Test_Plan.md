# SOFTWARE TESTING PLAN

## 1. Project Information

| Field | Details |
|---|---|
| Project Name | Software Testing Portfolio – SauceDemo |
| Application Under Test | SauceDemo (Swag Labs) |
| Application URL | https://www.saucedemo.com/ |
| Testing Type | Manual and Automated Testing |
| Automation Tool | Selenium WebDriver |
| Testing Framework | Pytest |
| Programming Language | Python |
| Team Size | 2 |
| Institution | MS Ramaiah Institute of Technology |
| Department | Information Science and Engineering |

## 2. Introduction

This project focuses on testing the functionality of the SauceDemo web application using manual and automated testing approaches. The objective is to verify that the application's major features work as expected and to identify and document any issues encountered during testing.

The project covers user authentication, product listing, product sorting, shopping cart operations, checkout functionality, and logout operations. Selenium WebDriver with Python and Pytest is used to automate selected test scenarios.

## 3. Objectives of Testing

The main objectives are:

1. Verify successful and unsuccessful login scenarios.
2. Validate product display and sorting functionality.
3. Test adding and removing products from the shopping cart.
4. Verify checkout form validation and order completion.
5. Test logout functionality and access restrictions after logout.
6. Execute manual and automated test cases.
7. Record test results and document any failures.
8. Generate an HTML automation execution report.

## 4. Scope of Testing

### 4.1 In-Scope Modules

| Module | Features to be Tested |
|---|---|
| Login | Valid credentials, invalid credentials, empty fields, locked-out user |
| Products | Product display and sorting by name and price |
| Shopping Cart | Add products, remove products, view cart, cart persistence |
| Checkout | Form validation, customer information, price verification, order confirmation |
| Logout | Logout operation, browser back navigation, access after logout, login again |

### 4.2 Out-of-Scope

- Backend database testing.
- Performance and load testing.
- Security penetration testing.
- Cross-browser compatibility testing.
- Mobile application testing.

## 5. Test Environment

| Component | Details |
|---|---|
| Operating System | Windows 11 |
| Browser | Google Chrome |
| Browser Version | Chrome 156 |
| Programming Language | Python 3.14.4 |
| Automation Tool | Selenium WebDriver |
| Testing Framework | Pytest 9.2.0 |
| HTML Reporting | pytest-html 4.2.0 |
| Code Editor | Visual Studio Code |
| Version Control | Git and GitHub |

## 6. Testing Approach

The project uses two testing approaches.

### 6.1 Manual Testing

Manual testing is performed by interacting directly with the SauceDemo application. Test cases are executed based on predefined steps, and actual results are compared with expected results.

The manual testing process includes:

- Preparing test cases.
- Executing test steps.
- Recording actual results.
- Assigning Pass or Fail status.
- Capturing screenshots as evidence.

### 6.2 Automated Testing

Selected test scenarios are automated using Selenium WebDriver with Python and Pytest.

The automation process includes:

- Opening the SauceDemo application.
- Locating and interacting with web elements.
- Performing login, product, cart, checkout, and logout operations.
- Validating expected application behaviour using assertions.
- Generating an HTML test execution report using pytest-html.

## 7. Test Case Design Techniques

The following test case design techniques are considered:

**1. Equivalence Partitioning**

Input values are divided into valid and invalid groups. For example, valid login credentials, invalid credentials, and empty login fields.

**2. Boundary Value Analysis**

Validation of required checkout fields using missing or empty input values, such as first name, last name, and postal code.

**3. State Transition Testing**

Verification of application behaviour when moving between states, such as logged out, logged in, product selection, shopping cart, checkout, and order confirmation.

**4. Decision Table Testing**

Verification of different combinations of login inputs and their corresponding application responses.

## 8. Test Execution Strategy

The testing process follows these stages:

1. Understand the application and identify major functional modules.
2. Prepare test cases for each module.
3. Execute manual test cases and capture screenshots.
4. Develop Selenium automation scripts.
5. Execute automated test cases using Pytest.
6. Generate and review the HTML automation report.
7. Document execution failures and confirmed defects, if any.
8. Prepare the final test execution summary.

## 9. Entry Criteria

Testing begins when:

- The SauceDemo application is accessible.
- Test scenarios and test cases are prepared.
- The required browser and testing environment are available.
- Selenium and Pytest dependencies are installed.

## 10. Exit Criteria

Testing is considered complete when:

- All planned manual test cases have been executed.
- Automated test scripts have been executed.
- Test results are documented.
- Screenshots and execution reports are maintained.
- Identified failures are documented.
- The final test execution summary is prepared.

## 11. Roles and Responsibilities

| Team Member | Responsibility |
|---|---|
| Muhammad Moosa (1MS23IS071) | Test case design, manual testing, Selenium automation, documentation |
| Parth Jakar (1MS23IS087) | Test case design, manual testing, test execution, documentation |

Both team members contribute to test execution, result verification, and project documentation.

## 12. Deliverables

The project deliverables include:

- Software Testing Plan.
- Manual Test Case Documents.
- Selenium Automation Scripts.
- Test Execution Summary.
- Defect Report.
- Screenshots of Test Execution.
- HTML Automation Test Report.
- GitHub Repository.

## 13. Conclusion

This testing plan defines the objectives, scope, environment, approach, and execution strategy for testing the SauceDemo web application. Combining manual testing with Selenium-based automation provides a structured approach to validating the application's major functional modules and documenting the testing results.