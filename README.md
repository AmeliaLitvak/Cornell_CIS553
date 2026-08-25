[README_CIS553.md](https://github.com/user-attachments/files/31428042/README_CIS553.md)
# Cornell CIS 553: Currency Exchange Project

## Overview

This repository contains the course project for **Cornell CIS 553**. The
project implements a command-line currency exchange application in
Python.

The program combines string processing, function decomposition,
assertions, web-service interaction, response parsing, currency
validation, numerical conversion, and unit testing. A user supplies a
source currency, destination currency, and amount; the application
queries Cornell's currency service and displays the converted amount.

## Project Structure

``` text
CIS-553/
├── currency.py
├── exchangeit.py
├── testcurrency.py
└── README.md
```

-   `currency.py` contains the currency-conversion logic and helper
    functions.
-   `exchangeit.py` provides the command-line user interface.
-   `testcurrency.py` contains unit tests for the currency module.

## Application Design

The project demonstrates how a larger application can be constructed
from small, independently testable functions:

``` text
String Helpers
      ↓
Response Parsing
      ↓
Web-Service Request
      ↓
Currency Validation
      ↓
Currency Exchange
      ↓
Command-Line Interface
```

## `currency.py`

The primary function is:

``` python
exchange(src, dst, amt)
```

The module also defines these helpers:

``` python
before_space(s)
after_space(s)
first_inside_quotes(s)
get_src(json)
get_dst(json)
has_error(json)
service_response(src, dst, amt)
iscurrency(currency)
```

### String Processing Helpers

`before_space(s)` returns the substring before the first space, while
`after_space(s)` returns everything after the first space.

`first_inside_quotes(s)` returns the first substring enclosed by double
quotes. If multiple quoted regions are present, only the first is
returned.

These functions use string searching and slicing and are later reused
while parsing responses from the currency service.

### Parsing Currency-Service Responses

The course service returns JSON-formatted strings containing fields such
as:

``` text
success
src
dst
error
```

`get_src(json)` extracts the source-currency description, and
`get_dst(json)` extracts the destination-currency description. The
implementations are designed to work even when the service varies the
amount of whitespace following colons.

`has_error(json)` examines the `error` field and returns a Boolean
indicating whether the service reported an error.

### `service_response(src, dst, amt)`

This function communicates with the online course currency service. It
constructs a request using the source currency, destination currency,
amount, and the course-service key, then retrieves the response with:

``` python
introcs.urlread(url)
```

Assertions enforce requirements such as alphabetic currency codes and a
numeric amount.

### `iscurrency(currency)`

This function determines whether a currency code is recognized by the
service. It requests a conversion from the currency to itself and checks
the returned response with `has_error()`.

### `exchange(src, dst, amt)`

This is the main conversion function. It:

1.  Checks the types and validity of the source and destination currency
    codes.
2.  Checks that the amount is an integer or float.
3.  Requests a conversion with `service_response()`.
4.  Extracts the destination value with `get_dst()`.
5.  Uses `before_space()` to separate the numerical amount from the
    currency name.
6.  Converts that numerical string to a `float`.
7.  Returns the converted amount.

This function illustrates how several smaller helpers can be combined
into a larger operation.

## `exchangeit.py`

`exchangeit.py` provides the command-line interface.

It prompts the user for:

1.  The three-letter code of the original currency
2.  The three-letter code of the destination currency
3.  The amount to convert

The amount is converted to a float and passed to:

``` python
currency.exchange(src, dst, amt_float)
```

The returned value is rounded to three decimal places and displayed to
the user.

A typical interaction follows this pattern:

``` text
3-letter code for original currency: USD
3-letter code for the new currency: EUR
Amount of the original currency: 10
You can exchange 10 USD for <converted amount> EUR.
```

The exact conversion depends on the response returned by the course
currency service.

## `testcurrency.py`

The test module contains dedicated procedures for:

``` python
test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()
```

If every assertion succeeds, the script prints:

``` text
All tests completed successfully
```

## Testing Strategy

The tests follow the functional layers of the application.

### String Helpers

The first tests cover cases such as spaces at the beginning or end of
strings, multiple spaces, empty quoted content, and multiple quoted
regions.

### Response Parsing

Tests for `get_src()`, `get_dst()`, and `has_error()` use both
successful and failed JSON-formatted responses and vary whitespace
around the fields.

### Service and Currency Validation

`test_service_response()` makes service requests using valid and invalid
currency codes and positive and negative amounts.

`test_iscurrency()` verifies both a recognized currency code and an
invalid example.

### Complete Exchange

`test_exchange()` checks the final exchange operation with positive and
negative amounts. Floating-point results are compared using:

``` python
introcs.assert_floats_equal()
```

## Preconditions and Assertions

Assertions enforce documented function requirements throughout the
project.

Examples include checking that an argument is a string, verifying that
currency codes contain alphabetic characters, and ensuring that exchange
amounts are numeric.

The final exchange function also checks whether currency codes are
actually recognized by the remote service. This distinguishes basic
structural validation from application-level validation.

## Functional Decomposition

The project is a strong example of functional decomposition:

``` text
exchange()
   |
   +-- iscurrency()
   |      |
   |      +-- service_response()
   |      +-- has_error()
   |
   +-- service_response()
   |
   +-- get_dst()
   |      |
   |      +-- first_inside_quotes()
   |
   +-- before_space()
```

Each helper performs a focused task and can be tested separately before
being incorporated into the complete conversion workflow.

## Data Flow

``` text
User
 ↓
exchangeit.py
 ↓
currency.exchange()
 ↓
Validate currencies
 ↓
service_response()
 ↓
Online currency service
 ↓
JSON-formatted response
 ↓
get_dst()
 ↓
before_space()
 ↓
Convert numeric text to float
 ↓
exchangeit.py
 ↓
Round and display result
```

## Requirements

-   Python 3
-   `introcs`
-   Internet access to the course currency service

The project uses `introcs` for string utilities, URL access, assertions
in the test suite, and floating-point comparisons.

## Running the Application

From the repository directory:

``` bash
python exchangeit.py
```

Enter the requested source currency, destination currency, and amount.

## Running the Tests

Run:

``` bash
python testcurrency.py
```

Some tests make requests to the remote course currency service, so they
require network access and continued availability of that service. Exact
exchange-rate values may also depend on the service data.

## Security Note

The supplied coursework stores a course-service API key directly in
`currency.py`.

For production software or private credentials, API keys should
generally not be committed to source control. Environment variables or
an appropriate secrets-management system are preferable. This README
intentionally does not reproduce the key.

## Key Concepts Demonstrated

-   Python functions
-   Function specifications
-   Preconditions and assertions
-   String searching and slicing
-   String parsing
-   Helper functions
-   Functional decomposition
-   JSON-formatted response processing
-   Web-service requests
-   Currency-code validation
-   Numeric and floating-point conversion
-   Command-line input and output
-   Unit testing
-   Edge-case testing
-   External-service integration

## Author

Amelia Litvak

## Course

Cornell CIS 553
