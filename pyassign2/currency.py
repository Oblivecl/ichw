##1700012622 2017/12/13###

##Function def###
"""Part for currency exchange

This part provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this part is exchange."""

#  A  #

'''Can't run while the space is at the beginning '''
def before_space(s):
    if s[0]!=" " :  
        a1=s.index(" ")
        a=s[:a1]
    return a 

'''This function will output all string after the first space'''         
def after_space(s):
    if s[0]!=" ":
        a1=s.index(" ")
        a=s[a1+1:]
    return a 

#  B  #

def first_inside_quotes(s):
    b1=s.index('"')
    b2=s.index('"',b1+1)
    b=s[b1+1:b2]
    return b
    
def get_from(jstr):
    b1=jstr.index("from")+5
    b=first_inside_quotes(jstr[b1:])
    return b

def get_to(jstr):
    b1=jstr.index("to")+3
    b=first_inside_quotes(jstr[b1:])
    return b

def has_error(jstr):
    b1=jstr.index("error")+6
    b=first_inside_quotes(jstr[b1:])
    return "" != b


#  C  #

from urllib.request import urlopen

def currency_response(currency_from, currency_to, amount_from):
    web1="http://cs1110.cs.cornell.edu/2016fa/a1server.php?"
    web2="from={0}&to={1}&amt={2}"\
    .format(currency_from, currency_to, amount_from)
    web=web1+web2
    doc = urlopen(web)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr


#  D  #
    
def iscurrency(currency):
    jstr = currency_response(currency,currency,1.0)
    d = not has_error(jstr)
    return d

def exchange(currency_from,currency_to,amount_from):
    d=currency_response(currency_from, currency_to, amount_from)
    to=float(before_space(get_to(d)))
    return to

#  Test  #
"""Unit test for module a1

When run as a script, this module invokes several procedures that 
test the various functions in the module a1."""

t1 = '{ "from" : "1 United States Dollar", "to" : "1 United States Dollar", '
t2 = '"success" : true, "error" : "" }'
t = t1+t2

def test_before_space():
    assert('It' == before_space('It is ok'))
def test_after_space():
    assert('is ok' == after_space('It is ok')) 
def test_first_inside_quotes():
    assert('from' == first_inside_quotes(t))
def test_get_from():
    assert('1 United States Dollar' == get_from(t))
def test_get_to():    
    assert('1 United States Dollar' == get_to(t))
def test_has_error():    
    assert(False == has_error(t))
def test_currency_response():    
    assert(t == currency_response('USD','USD',1.0))
def test_iscurrency():    
    assert(False == iscurrency('123'))
def test_exchange():    
    assert(1.0 == exchange('USD','USD',1.0))
    
def testAll():
    """test all cases"""
    test_before_space()
    test_after_space()
    test_first_inside_quotes()
    test_get_from()
    test_get_to()
    test_has_error()
    test_currency_response()   
    test_iscurrency()
    test_exchange()
    print("All tests passed")

testAll()

    
    
    
    
    