
# Test Execution Summary

## 1. Project Information

- **Application:** SauceDemo (Swag Labs)
- **Application URL:** https://www.saucedemo.com/
- **Testing Type:** Manual Testing and Automated Testing
- **Automation Tool:** Selenium WebDriver
- **Programming Language:** Python
- **Testing Framework:** Pytest
- **Browser:** Google Chrome

## 2. Testing Modules

The following modules were tested:

1. Login
2. Product Listing and Sorting
3. Shopping Cart
4. Checkout
5. Logout and Session Management

## 3. Manual Testing Results

| Module | Test Cases | Result |
|---|---:|---|
| Login | 5 | All Passed |
| Products and Sorting | 5 | All Passed |
| Shopping Cart | 8 | All Passed |
| Checkout | 7 | All Passed |
| Logout | 5 | All Passed |
| **Total** | **30** | **All Passed** |

## 4. Automated Testing Results

| Module | Automated Tests | Passed |
|---|---:|---:|
| Login | 5 | 5 |
| Products and Sorting | 5 | 5 |
| Shopping Cart | 7 | 7 |
| Checkout | 7 | 7 |
| Logout | 5 | 5 |
| **Total** | **29** | **29** |

## 5. Consolidated Automation Execution

The consolidated execution generated the following results:

- Total tests: 29
- Passed: 28
- Failed: 1
- Pass percentage: 96.55%


The failed test case was test_browser_back_after_logout. It encountered a Selenium TimeoutException while waiting for the Logout button to become clickable. No application defect was confirmed from this execution. The individual module executions had passed in their respective runs.

## 6. Testing Tools

- Python
- Selenium WebDriver
- Pytest
- pytest-html
- Visual Studio Code
- Google Chrome

## 7. Conclusion

Manual testing was completed across all five application modules, and all recorded manual test cases passed.

Automated testing was implemented using Selenium WebDriver and Pytest. The individual module executions passed. During the consolidated execution, 28 tests passed and one test failed due to a Selenium TimeoutException while waiting for the Logout button to become clickable.

The testing activities provided coverage of login validation, product sorting, cart operations, checkout validations, order completion, and logout/session management.
