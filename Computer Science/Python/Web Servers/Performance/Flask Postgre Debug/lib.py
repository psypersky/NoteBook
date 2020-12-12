
# ''.join([chr(ord(c) + 1) for c in 'abcd'])

# functools.reduce(lambda acc, i: acc + chr(ord(i) + 1),'abcd', '')

def encrypt_string(string_to_encrypt):
    return ''.join(list(map(lambda c: chr(ord(c) + 1), string_to_encrypt)))

def encrypt_user(user_tupl):
  return (
    user_tupl[0],
    encrypt_string(user_tupl[1]),
    encrypt_string(user_tupl[2])
  )

def encrypt_users(users_list):
  return list(map(lambda u: encrypt_user(u), users_list))
