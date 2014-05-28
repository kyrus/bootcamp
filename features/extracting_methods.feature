Feature: Extracting Method


Scenario Outline: 
	Given the file is a "<type>"
	When given to an "<extractor>"
	Then the file should be "<response>"

Examples:
	|  type			|  extractor		|  response								|
	|  zip			|  zip_extractor	|  directory with unzipped archive file	|
	|  gpg			|  zip_extractor	|  exception 							|
	|  gzip			|  gzip_extractor	|  directory with unzipped archive file |
