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
These are the setups to be followed 
