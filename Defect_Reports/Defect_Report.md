# Defect Report

## 1. Application Information

- Application: SauceDemo (Swag Labs)
- Application URL: https://www.saucedemo.com/
- Testing Type: Manual and Automated Testing

## 2. Defect Summary

During the testing activities, no confirmed application defects were identified in the executed test scenarios.

All recorded manual test cases passed.

## 3. Automation Execution Issue

| Field | Details |
|---|---|
| Issue ID | EXEC-001 |
| Issue Type | Automation Execution Failure |
| Environment | Windows 11, Google Chrome, Selenium WebDriver |
| Test Case | test_browser_back_after_logout |
| Description | Selenium encountered a TimeoutException while waiting for the Logout button to become clickable. |
| Impact | One test failed during consolidated automation execution. |
| Application Defect | Not confirmed |
| Status | Documented |

## 4. Conclusion

No confirmed functional defects were identified during the executed manual and automated test scenarios.

One automated test encountered a Selenium TimeoutException during consolidated execution. This was documented as an automation execution issue rather than a confirmed application defect.