Feature: Extracting Method

Scenario Outline: Successfully extracting files of different types
    Given I have a file of type "<type>"
    When I run the extractor "<extractor>"
    Then I should get a directory that contains the contents of the archive

Examples:
    |  type            |  extractor |
    |  zip             |  Zip       |
    |  gz              |  Gzip      |

Scenario Outline: Unsuccessfully extracting files of different types
    Given I have a file of type "<type>"
    When I run the extractor "<extractor>"
    Then I should get an error message

Examples:
    |  type            |  extractor |
    |  zip             |  Gzip      |
    |  gpg             |  Zip       |
    |  gz              |  Zip       |
