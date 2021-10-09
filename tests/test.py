from most_active_cookie import match_date
from ..most_active_cookie import *

def test_match_date():
    assert (match_date('2018-12-09T00:000:000', '2018-12-09') 
    and not match_date('2019-12-09T01:120:21', '2018-12-09')
    and not match_date('asjdkfls;dlkj', '2018-12-09')
    and not match_date('01:0013:01T2018-12-09', '2018-12-09'))

def test_update_count():
    cookie_dict = {'a': 1,'b': 2,'c' : 6}
    assert (update_count('a', cookie_dict) == 2 
    and update_count('d', cookie_dict) == 1)

def test_parse_csv():
    max_cookies_1 = parse_csv('./tests/test_cookies_single.csv', '2018-12-09')
    max_cookies_2 = parse_csv('./tests/test_cookies_multi.csv', '2018-12-09')
    assert (max_cookies_1 == ['c1'] and len(max_cookies_2) == 2 and max_cookies_2 == ['c1', 'c2'])



