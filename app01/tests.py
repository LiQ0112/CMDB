from django.test import TestCase

# Create your tests here.
s = {
    'csrfmiddlewaretoken': ['F3NsRcQOKC5IixN5NVIBy5J2NQxbNd0Kw7znAYxEjlGNFRGpi47I94gujrdutnFo'],
    'classes': ['9'],
    'depart': ['1'],
    'name': ['egon'],
    'SN': ['1232131231'],
    'date': ['2020-06-02'],
    'repairs': ['213123'],
    'error_description': ['123123'],
    'service_person': ['1231'],
    'service_type': ['1'],
    'service_cost': ['1231'],
    'service_result': ['123123']
    }
s.pop("csrfmiddlewaretoken")
for k in s:
    print(k,'*',s[k])