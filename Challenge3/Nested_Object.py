###############################################################################
#Python script for KPMG Challenge                                             #
#File Name: Nested_Object.yml                                                 #
###############################################################################
#Developer - Arun Kumar Lakshmi Narayanan                                     #
###############################################################################
#Purpose Of The Script : Display the value of the key provided as input from  #
#                        user                                                 #
###############################################################################
import json
#Get the object and key from user
str_inputobj = input("Please provide your JSON object:")
str_keysearch = input("Please provide your Key for search:")

def extract_values(obj, key):
#    Pull all values of specified key from nested JSON.
    arr = []

    def extract(obj, arr, key):
#       Recursively search for values of key in JSON tree.
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results
    
result_value = extract_values(str_inputobj.json(), str_keysearch)
print("The value of the key provided for search is:" + result_value)