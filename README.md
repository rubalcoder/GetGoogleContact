# GetGoogleContact
This document explain the process to list and fetch the contact list of a User from google contacts. Google provide a set of APIs (Google people API) to perform set of CRUD operations. End users
and developers community can access the APIs to develop an application.

Test_GetContacList.py
==========================================================
This is a sample python module/script to download the contact List from Google contacts, save it locally into a JSON file "contactList.json". The script also includes test cases to verify and validate
the contactList data, reponse and files.
The script uses python request library to fetch data from Google contacts for the specified user, JSON module to serialize/deserialize the http response and save it to a JSON file, execute test cases with
parameterized test data and execute pytest test cases with setup teardown according to pytest fixtures.

PreRequirements:
==========================================================
The APIs can only be used when they are enabled for the user. Below is the link with information of APIs and how to use them
https://developers.google.com/people

List of People RestAPIs used directly in the code is as follows:
https://developers.google.com/people/api/rest/v1/people/searchContacts

Before start coding your first client application,  need to do three things:
1. Get a Google Account
2. Create a project, Enable the Google PeopleAPI for the account
3. Configure the OAth 2.0 authorisation
4. Create Credentials with google people API enabled and OAuth 2.0 authentication
5. Set up your app
Please follow up the more details: https://developers.google.com/people/v1/getting-started

The contact List is fetched using Request Library in python which uses Http restAPIs. The authentication is done using personal access tokens generated using POSTMAN tool.
Please follow the document https://www.linkedin.com/pulse/access-google-drive-rest-apis-using-oauth2-postman-haris-saleem/
Once the Authentication code is generated copy the Token inside the file

Setup:
===========================================================
These are the setups need to be executed to update all the dependencies before executing the main test script.

1. Install the python request library: pip install requests
2. Install the python pytest module: pip install pytest
3. Install the pytest-html library to generate the reports: pip install pytest-html

Once all the Libraries are updated Open the Test_GetContactList.py and update as follows:
1. Configuration parameters are updated in the begining with Http request URL, payload, headers etc. Need to update these parameters according the user
   Note: The Http RestAPI will remain the same for get contact list only the PATSTOKEN will change
2. The second set includes data for test parameterization and data driven testing. This data may differ according the contact list of the Individual users

TestExample:
============================================================
Once the all prerequisits and setup is done. Actual test cases are executed as follows.

#pytest "Test_GetContactList.py" -s --html==report.html
The above command is executed in the command line and the script will execute. Pytest will collect all the test cases defined in form of test methods, starting with
test_ or ending with _test.
These test are parameterised  with test data and the setup functions are declared in form of fixture

#pytest "Test_GetContactList.py" -m smoke -s --html==report.html
The above command will collect all the test cases but execute only the test cases marked as smoke

Flags:
pytest: This keyword is used to detect all test cases in the package/module/script with pytest format
-s: This flag is used to redirect outputs to console for "print" statements
-m: flag with mark parameter used to mark and execute specific test cases
--html: flag with a parameter to generate a report for the complete execution

End Result and Artifacts:
=============================================================
1. The test results are available on the console and HTML report with pass/fail/Error information for each test cases
2. For test cases failing in assertion statements the reason and error is available on the console and html report
3. ContactList.json file is avaialble in the current working directory
4. Html report with pass/Fail/Error information available for each test case
