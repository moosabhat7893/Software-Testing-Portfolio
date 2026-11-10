# Software Testing Portfolio – SauceDemo

## 1. Project Overview

This project demonstrates manual and automated software testing of the SauceDemo (Swag Labs) online shopping application.

The objective is to evaluate the functionality of the application through structured test planning, test case design, test execution, defect documentation and browser automation.

**Application:** SauceDemo  
**Application URL:** https://www.saucedemo.com/
## 2. Team Members

| S. No. | Name | USN |
|---|---|---|
| 1 | Muhammad Moosa | 1MS23IS071 |
| 2 | Parth Jakar | 1MS23IS087 |

**Team Size:** 2
**Institution:** MS Ramaiah Institute of Technology
**Department:** Information Science and Engineering

## 3. Testing Objectives

- Verify the login functionality and input validations.
- Test product listing and sorting functionality.
- Verify shopping cart operations.
- Validate checkout information and order completion.
- Test logout and session management.
- Automate selected test scenarios using Selenium WebDriver.

## 4. Application Modules Tested

1. Login
2. Product Listing and Sorting
3. Shopping Cart
4. Checkout
5. Logout and Session Management

## 5. Tools and Technologies

| Tool | Purpose |
|---|---|
| Python | Automation programming language |
| Selenium WebDriver | Browser automation |
| Pytest | Test execution framework |
| pytest-html | HTML test reporting |
| Visual Studio Code | Development environment |
| Google Chrome | Browser under test |
| Git and GitHub | Version control and project hosting |

## 6. Testing Approach

The project includes:

- Manual test case design and execution.
- Equivalence partitioning and boundary value analysis where applicable.
- Functional testing and input validation.
- Selenium-based browser automation.
- Automated test execution using Pytest.
- HTML test report generation.
- Defect and execution issue documentation.

## 7. Project Structure

```text
Software_Testing_Portfolio/
│
├── Automation/
│   ├── tests/
│   │   ├── test_login.py
│   │   ├── test_products.py
│   │   ├── test_cart.py
│   │   ├── test_checkout.py
│   │   └── test_logout.py
│   └── requirements.txt
│
├── Screenshots/
├── Test_Case_Design/
├── Test_Execution/
│   └── Test_Execution_Summary.md
├── Test_Reports/
│   └── automation_report.html
├── Defect_Reports/
│   └── Defect_Report.md
│
├── .gitignore
└── README.md
```

## 8. Test Execution Results

### Manual Testing

- Total test cases: 30
- Passed: 30

### Automated Testing

Individual module executions:
- Total automated test cases: 29
- Individual module executions passed in their respective runs.

Consolidated execution:
- Total: 29
- Passed: 28
- Failed: 1
- Pass percentage: 96.55%

The failed test case was test_browser_back_after_logout. It encountered a Selenium TimeoutException while waiting for the Logout button to become clickable. No application defect was confirmed from this execution.

## 9. How to Run the Automation Tests

### Step 1: Clone the repository

```bash
git clone https://github.com/moosabhat7893/Software-Testing-Portfolio.git
```

### Step 2: Navigate to Automation

```bash
cd Automation
```

### Step 3: Create a virtual environment

```bash
python -m venv venv
```

### Step 4: Activate the environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 5: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Execute the tests

```bash
python -m pytest tests/ -v
```

### Step 7: Generate an HTML report

```bash
python -m pytest tests/ -v --html=automation_report.html --self-contained-html
```

## 10. Defect Reporting

No confirmed application defects were identified during the executed test scenarios.

One automated test encountered a Selenium TimeoutException during consolidated execution while waiting for the Logout button to become clickable. No confirmed application defect was identified. This execution issue is documented separately in the Defect Reports folder.

## 11. Conclusion

This project provided practical experience in software testing, including test planning, manual test execution, test case design, Selenium automation, Pytest execution and HTML reporting.

The project demonstrates the application of software testing techniques to an online shopping application and provides documented evidence of the testing activities performed.