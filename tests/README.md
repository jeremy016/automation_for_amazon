# Tests

## Test Scenarios

### Login

[Positive]

- [x] Verify that all the elements and controls including text-boxes, buttons, and links are present on the Login page.
- [x] Verify if a user will be able to login with a valid username and valid password.
- [-] Verify the ‘Forgot Password’ functionality.
- [-] Verify the 'remember me' functionality.
- [x] Verify that the password is in masked form when entered.
- [x] Verify that the user is able to login by entering valid credentials and pressing Enter key.
- [x] Verify that closing the browser should not log-out an authenticated user. Launching the application should lead the user to login state only. 
- [x] Verify that once logged in, clicking the back button doesn’t logout the user.


[Negative]
- [x] Verify the error messages with invalid account.
- [x] Verify that the validation message gets displayed in case the user leaves the username or password field as blank.
- [x] Verify that the user is not able to login with an valid username and invalid password.