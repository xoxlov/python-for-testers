Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <middlename> , <lastname>, <address>, <email>, <homephone> and <mobilephone>
  When I add the contact to the list
  Then the new contact list is equal to the old list with added contact

  Examples:
  | firstname   | middlename | lastname   | address   | email         | homephone  | mobilephone |
  | Andrey      | A.         | Vinogradov | Moscow    | andrey@che.ru | 789456     |             |
  | firstname01 | midname    | lastname01 | Konakovo  | email01       | 4824244424 | 89151662781 |

Scenario: Delete random contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without deleted contact

Scenario: Update random contact
  Given a non-empty contact list
  Given a random contact from the list
  Given a contact with <firstname>, <lastname>, <address>, <email> and <homephone>
  When I update the random contact from the list with the new contact data
  Then the modified contact list is equal to the old list with updated contact data

  Examples:
  | firstname | lastname | address | email      | homephone   |
  | Alexander | Pavlov   | Moscow  | newmail@ru | 81234567890 |
