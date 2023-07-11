user_profile = {
    # default values
    'name' : 'N/A',
    'email' : 'N/A',
    'phone' : 'N/A'
}

user_input = {
    'name' : 'Bob',
    'phone' : '123-456-7890',
    'gender' : 'female'
}

user_profile |= user_input
# profile.update(user_input)
# profile = {**profile, **user_input}

print(user_profile)