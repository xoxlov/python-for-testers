*** Settings ***
Library  rf.ContactBook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures


*** Test Cases ***
Add new contact
    ${old_list}=  Get Contact List
    ${contact}=  New Contact  FirstName1  LastName1
    Create Contact  ${contact}
    ${new_list}=  Get Contact List
    Append To List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

Delete contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    Delete Contact  ${contact}
    ${new_list}=  Get Contact List
    Remove Values From List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

Update contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact_to_update}=  Get From List  ${old_list}  ${index}
    ${contact_with_new_data}=  New Contact  FirstNameUpdated  LastNameUpdated
    Update Contact  ${contact_to_update}  ${contact_with_new_data}
    ${new_list}=  Get Contact List
    Update Value In List  ${old_list}  ${contact_to_update}  ${contact_with_new_data}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}
