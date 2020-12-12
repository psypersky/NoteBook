
def encrypt_string(string_to_encrypt):
    # ''.join(list(map(lambda c: chr(ord(c) + 1), string_to_encrypt)))
    # functools.reduce(lambda acc, i: acc + chr(ord(i) + 1),'abcd', '')
    # ''.join([chr(ord(c) + 1) for c in 'abcd'])
    return ''.join(chr(ord(c) + 1) for c in string_to_encrypt)

def encrypt_user(user_tupl):
  return (
    user_tupl[0],
    encrypt_string(user_tupl[1]),
    encrypt_string(user_tupl[2])
  )

def encrypt_users(users_list, times = 1):
  i = 0
  encrypted_users = None

  while (i < times):
    encrypted_users = list(map(lambda u: encrypt_user(u), users_list))
    i = i + 1

  return encrypted_users