"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author:Amelia Litvak
Date:07/17/2025
"""
import introcs
import currency
def test_before_space():
    """Test procedure for before_space"""
    print('Testing before_space')
    result=currency.before_space(' hello')
    introcs.assert_equals('',result)
    result=currency.before_space('h e l l o')
    introcs.assert_equals('h',result)
    result=currency.before_space('he llo')
    introcs.assert_equals('he',result)
    result=currency.before_space('hel  lo')
    introcs.assert_equals('hel',result)


def test_after_space():    
    """Test procedure for after_space"""
    print('Testing after_space')
    result=currency.after_space(' hello')
    introcs.assert_equals('hello',result)
    result=currency.after_space('hello ')
    introcs.assert_equals('',result)
    result=currency.after_space('he  llo')
    introcs.assert_equals(' llo',result)
    result=currency.after_space('h e l l o')
    introcs.assert_equals('e l l o',result)


def test_first_inside_quotes():
    """Test procedure for first_inside_quotes"""
    print('Testing first_inside_quotes')
    result=currency.first_inside_quotes('"hi"')
    introcs.assert_equals('hi',result)
    result=currency.first_inside_quotes('"h"i')
    introcs.assert_equals('h',result)
    result=currency.first_inside_quotes('""hi')
    introcs.assert_equals('',result)
    result=currency.first_inside_quotes('"h""i"')
    introcs.assert_equals('h',result)


def test_get_src():
    """Test procedure for get_src"""
    print('Testing get_src')
    result=(currency.get_src('{"success": true, "src": "2 United \
States Dollars", "dst": "1.772814 Euros", "error": ""}'))
    introcs.assert_equals('2 United States Dollars',result)
    result=currency.get_src('{"success":false,"src":"","dst":"","error":\
"Source currency code is invalid."}')
    introcs.assert_equals('',result)
    result=currency.get_src('{"success":false,"src":  "","dst":"","error":\
"Source currency code is invalid."}')
    introcs.assert_equals('',result)
    result=currency.get_src('{"success": true, "src":"2 United States Dollars"\
, "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars',result)


def test_get_dst():
    """Test procedure for get_dst"""
    print('Testing get_dst')
    result=currency.get_dst('{"success": true, "src": "2 United States Dollars",\
 "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros',result)
    result=currency.get_dst('{"success":false,"src":"","dst": "","error":\
"Source currency code is invalid."}')
    introcs.assert_equals('',result)
    result=currency.get_dst('{"success":false,"src":  "","dst":""\
,"error":"Source currency code is invalid."}')
    introcs.assert_equals('',result)
    result=currency.get_dst('{"success": true, "src":\
"2 United States Dollars", "dst":"1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros',result)


def test_has_error():
    """Test procedure for has_error"""
    print('Testing has_error')
    result=currency.has_error('{"success": true, "src": "2 United States Dollars"\
, "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals(False,result)
    result=currency.has_error('{"success":false,"src":"","dst": "","error":\
"Source currency code is invalid."}')
    introcs.assert_equals(True,result)
    result=currency.has_error('{"success":false,"src":  "","dst":"","error":\
 "Source currency code is invalid."}')
    introcs.assert_equals(True,result)
    result=currency.has_error('{"success": true, "src":"2 United States Dollars"\
, "dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals(False,result)


def test_service_response():
    """Test procedure for service_response"""
    print('Testing service_response')
    result=currency.service_response('USD','EUR',2.5)
    introcs.assert_equals('{"success": true, "src": "2.5 United States Dollars",\
 "dst": "2.2160175 Euros", "error": ""}',result)
    result=currency.service_response('ABC','USD',2.5)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error":\
 "The rate for currency ABC is not present."}',result)
    result=currency.service_response('AFN','USD',-2.5)
    introcs.assert_equals('{"success": true, "src": "-2.5 Afghan Afghanis",\
 "dst": "-0.031132778861032443 United States Dollars", "error": ""}',result)
    result=currency.service_response('USD','ABC',-2.5)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error":\
 "The rate for currency ABC is not present."}',result)


def test_iscurrency():
    """Test procedure for iscurrency"""
    print('Testing iscurrency')
    result=currency.iscurrency('USD')
    introcs.assert_equals(True,result)
    result=currency.iscurrency('ABC')
    introcs.assert_equals(False,result)


def test_exchange():
    """Test procedure for exchange"""
    print('Testing exchange') 
    result=currency.exchange('USD','EUR',1)
    introcs.assert_floats_equal(0.886407, result)
    result=currency.exchange('USD','EUR',-1)
    introcs.assert_floats_equal(-0.886407, result)


test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()
print('All tests completed successfully')


