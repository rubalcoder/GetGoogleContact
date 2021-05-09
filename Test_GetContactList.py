import os
import json
import requests
import pytest


BaseUrl = 'https://people.googleapis.com/v1/people/me/connections'
Parameters = ['phoneNumbers', 'names', 'emailAddress']
payload = {}
headers = {
  'Authorization': 'Bearer ya29.a0AfH6SMCjkrDurR-z0yruJ5xrzZ8XxYP4-z2mZZcKOumT2L-hdfG6_S40y0-eZRAkGKrRTwtxScoSbAq9fuP4M0_J7G3Lw-Ekilpz_ciIHQ_uQwXkgyQ94t1oSzVNmbW1cnQf_pKpSgzhLaYasMerlImfR66Q'
}


@pytest.fixture
def getContactList():
    url = BaseUrl+"?personFields=names"
    response = requests.request("GET", url, headers=headers, data=payload)
    jsonResponse = json.loads(response.text)
    return [response.status_code, jsonResponse]


@pytest.fixture
def getDataFromJson():
    file1 = open("ContactList.json", "r")
    rJson = json.load(file1)
    file1.close()
    return rJson


@pytest.mark.usefixtures("getContactList")
class Test_ValidateContactList:

    def test_validateResponse(self, getContactList):
        assert getContactList[0] == 200 , "request not successfull"

    def test_validateResponsetype(self, getContactList):
        assert type(getContactList[1]) == dict , "response Invalid"

    def test_createVerifyContactListFile(self, getContactList):
        fileObj = open("ContactList.json", "w")
        json.dump(getContactList[1], fileObj)
        fileObj.close()
        assert os.path.isfile("ContactList.json") , "File did not create successfully"

    def test_verifyTestCaseCountMatch(self, getContactList, getDataFromJson):
        assert getContactList[1] == getDataFromJson , "Data Mismatch"

    def test_verifyDataMatchFileandtext(self, getContactList, getDataFromJson):
        assert len(getContactList[1]['connections'][0]['resourceName']) == len(getDataFromJson['connections'][0]['resourceName']), "Data Mismatch"


@pytest.fixture()
def getContactListWithParameters():
    url = BaseUrl+"?personFields=phoneNumbers,names,emailAddresses"
    response = requests.request("GET", url, headers=headers, data=payload)
    jsonResponse = json.loads(response.text)
    return jsonResponse


@pytest.mark.usefixtures("getContactListWithParameters")
class Test_ValidateDataContactList:


    @pytest.mark.parametrize('name', ["Dilip Gutthi", 'ross taylor', 'Chaudhary Uncle'])
    def test_verifyNamesInJsonResponse(self, getContactListWithParameters, name):
        count = 0
        for i in range (0, len(getContactListWithParameters['connections'])):

            if name in list(getContactListWithParameters['connections'][i]['names'][0].values()):
                count = count+1
                break
        if count > 0:
            assert True
        else:
            assert False , name + " does not exist in the contact list"












