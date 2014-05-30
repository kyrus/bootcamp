Feature: Extractor Detector

Scenario Outline: Successfully determine the right extractor for different file types
    Given I have a file of type "<type>"
    When I determine the extractor to use on the file
    Then I should be using the "<extractor>" extractor

Examples:
    |  type            |  extractor |
    |  zip             |  Zip       |
    |  gz              |  Gzip      |
    |  7z              |  7zip      |
    |  tar             |  Tar       |
    |  rar             |  Rar       |
