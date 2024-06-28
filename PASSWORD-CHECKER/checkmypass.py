import requests
import hashlib
import sys

#  DEFINE FUNCTION THAT GOES TO WEB TO CHECK THE HASH DATA 


# Constructs the URL using the base URL https://api.pwnedpasswords.com/range/ and appends query_char.
# Sends a GET request to this URL using requests.get().
# Checks if the response status code (res.status_code) is 200 (OK). If not, it raises a RuntimeError.
# Returns the response object (res).

def request_api_data(query_char):
    url='https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching:{res.status_code}, check the api and try again')
    return res


# Converts the response (hashes.text) into lines (splitlines()).
# Splits each line by : to separate the hash suffix (h) and the count (count).
# Iterates through these pairs (h, count) and checks if h matches hash_to_check.
# If a match is found, returns the count (number of times the password hash has been leaked).
# # If no match is found, returns 0.
# CHECK THE STRING PASSWORD THAT HASHED IN DATAlines

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

# Computes the SHA-1 hash of password encoded in UTF-8 and converts it to hexadecimal (hexdigest()). The result is converted to uppercase.
# Splits the hash into first5_char (first 5 characters of the hash) and tail (remaining characters).
# Calls request_api_data to get the response from the API for first5_char.
# Calls get_password_leaks_count to parse the response and find the count of occurrences of tail in the API response.
# # this function to check hash data in library

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf=8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response,tail)

# IF IT EVER USED THEN print
# Iterates through each password in args (which are command-line arguments).
# Calls pwned_api_check for each password to check if it has been leaked.
# Prints a message indicating whether the password was found in breaches or not.
# Returns 'done!' after processing all passwords
def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... ypu should not use this')
        else:
            print(f'{password} was not found .carry on!')
        return 'done!'
    
if __name__ == "__main__":
    main(sys.argv[1:])

