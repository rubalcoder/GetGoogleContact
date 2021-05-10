# Python Module to download Google Contacts on local system and verify and validate the contacts
# Python Request Library used to execute CRUD operations with HTTP RestAPi published by Google
# Json Library used to serialize/deserialize response data into JSON format
# Code Written in Python 3.7
# Pytest Framework used to collect and execute test cases in the module
# Start with importing the external modules and libraries into the main module
#
#
import os
import json
import requests
import pytest

# Declare the configuration parameters at the start of the script
# PatsToken or personal access token is generated to authorize the http communication over RestAPi, follow readme for more info
BaseUrl = 'https://people.googleapis.com/v1/people/me/connections'
PatsToken = 'ya29.a0AfH6SMAqFhch7jfCGtO7cU_Hvi7TjoB9tqI4sGh7Iy2AL5lpXPJn8DxPWKUGrbZOxQ7oh74c4I3fYn8FQDRrtH2eSEtq69GR19shSH4XnqGuisV8Sq2u27m7LCS_AUYrsKy3QAQJGGcZXREGoywQhkjfNhZk0g'
payload = {}
headers = {'Authorization': 'Bearer '+PatsToken}

# Declare the Test data to parameterize test cases and perform data driven test sets
Parameters = ['phoneNumbers', 'names', 'emailAddress']
Parameters_Name = ["Dilip Gutthi", 'ross taylor', 'Chaudhary Uncle']
Parameters_PhoneNumber = ['012345', '23456', '78902']
Parameters_EmailAddress = ['a@sample.com', 'b@sample.com', 'c@sample.com']


@pytest.fixture
def getContactList():
    '''Function declared as a fixture to get the contact list with a mask parameter as name  '''
    url = BaseUrl+"?personFields=names"
    response = requests.request("GET", url, headers=headers, data=payload)
    jsonResponse = json.loads(response.text)
    return [response.status_code, jsonResponse]


@pytest.fixture
def getDataFromJson():
    '''Function declared as a fixture to get the contact list information from JSON file'''
    file1 = open("ContactList.json", "r")
    rJson = json.load(file1)
    file1.close()
    return rJson


@pytest.mark.usefixtures("getContactList")
class Test_ValidateContactList:
    '''Pytest test Class created with different test methods wrapped inside he class to download and validate the
    contactList with test cases associated to fixture, some of the test cases marked as smoke.
    Assert statements available to validate the tests'''

    @pytest.mark.smoke
    def test_validateResponse(self, getContactList):
        assert getContactList[0] == 200 , "request not successfull"

    def test_validateResponsetype(self, getContactList):
        assert type(getContactList[1]) == dict , "response Invalid"

    def test_createVerifyContactListFile(self, getContactList):
        fileObj = open("ContactList.json", "w")
        json.dump(getContactList[1], fileObj)
        fileObj.close()
        assert os.path.isfile("ContactList.json") , "File did not create successfully"

    @pytest.mark.smoke
    def test_verifyContactListCountMatch(self, getContactList, getDataFromJson):
        assert getContactList[1] == getDataFromJson , "Data Mismatch"

    def test_verifyDataMatchFileandtext(self, getContactList, getDataFromJson):
        assert len(getContactList[1]['connections'][0]['resourceName']) == len(getDataFromJson['connections'][0]['resourceName']), "Data Mismatch"


# Pytest fixture to fetch data according to the personFields mask
@pytest.fixture()
def getContactListWithParameters():
    url = BaseUrl+"?personFields=phoneNumbers,names,emailAddresses"
    response = requests.request("GET", url, headers=headers, data=payload)
    jsonResponse = json.loads(response.text)
    return jsonResponse


@pytest.mark.usefixtures("getContactListWithParameters")
class Test_ValidateDataContactList:
    '''pytest test class with test cases wrapped and paramterized to validate the data against the data set parameters'''


    @pytest.mark.parametrize('name', Parameters_Name)
    def test_verifyNamesInJsonResponse(self, getContactListWithParameters, name):
        '''Pytest test case to validate the contact names inside the contactList. Test case execute multiple times
        according to the parameterized data '''
        count = 0
        for i in range (0, len(getContactListWithParameters['connections'])):

            if name in list(getContactListWithParameters['connections'][i]['names'][0].values()):
                count = count+1
                break
        if count > 0:
            assert True
        else:
            assert False , name + " does not exist in the contact list"

    @pytest.mark.smoke
    @pytest.mark.parametrize('phoneNumber', Parameters_PhoneNumber)
    def test_verifyNamesInJsonResponse(self, getContactListWithParameters, phoneNumber):
        '''Pytest test case to validate the contact phoneNumbers inside the contactList '''
        count = 0
        for i in range(0, len(getContactListWithParameters['connections'])):

            if phoneNumber in list(getContactListWithParameters['connections'][i]['phoneNumbers'][0].values()):
                count = count + 1
                break
        if count > 0:
            assert True
        else:
            assert False, phoneNumber + " does not exist in the contact list"

    @pytest.mark.parametrize('email', Parameters_EmailAddress)
    def test_verifyNamesInJsonResponse(self, getContactListWithParameters, email):
        '''Pytest test case to validate the contact emailAddress inside the contactList '''
        count = 0
        for i in range(0, len(getContactListWithParameters['connections'])):

            if email in list(getContactListWithParameters['connections'][i]['emailAddress'][0].values()):
                count = count + 1
                break
        if count > 0:
            assert True
        else:
            assert False, email + " does not exist in the contact list"


class Test_verifyDataAccordingToParameters:
    '''Test class to validate the data according to paramters passed in the test case. Parameters used is
    personFields masks according to the google API docs'''

    @pytest.mark.smoke
    @pytest.mark.parametrize('params', Parameters)
    def test_DataAccordingToParamenters(self, params):
        # Parameterised test case executing multiple times according to number of test parameters
        url = BaseUrl + "?personFields=" + params
        response = requests.request("GET", url, headers=headers, data=payload)
        jsonResponse = json.loads(response.text)
        count = 0
        if params in jsonResponse['connections'][0].keys():
            count += 1
        if count > 0:
            assert True
        else:
            assert False, params + " does not exist in the contact list"













