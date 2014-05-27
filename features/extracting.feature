Feature:
    As a data analyst
    I need to be able to run the Extract-O-Matic from the command line
    So that I can use it to extract files

Scenario: Run from the command line with no args
    When I run the Extract-O-Matic with the args ""
    Then I should see a usage message

