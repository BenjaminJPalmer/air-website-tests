# air-website-tests

A basic selection of tests for testing template WordPress websites using SeleniumBase in Python. Run via `pytest -s --headless --save-screenshot` for best performance as well as to save the screenshots to logs automatically.

## test_pagespeed.py

Three test cases to check the pagespeed of a site.

## test_validation.py

Test the HTML and CSS validation of the site

## TODO

* Improve screenshot functionality so `--save-screenshot` is not required
* Add more test cases as required
