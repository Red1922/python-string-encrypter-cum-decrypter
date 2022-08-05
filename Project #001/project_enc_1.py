import string
import random

root_key = ' ' + string.ascii_letters + string.digits + string.punctuation
gen_key = ''

content2 = []

encrypted_content1 = []


def generate_key():
  shuffled_buffer = list(root_key)
  random.shuffle(shuffled_buffer)
  gen_key = ''.join(shuffled_buffer)
  return gen_key


def encrypter(content1):
  current_key = generate_key()
  for item1 in content1:
    item2 = list(current_key)[root_key.index(item1)]
    encrypted_content1.append(item2)
  print("Original Text ===>", content1, "; Encrypted Info ===>",
        ''.join(encrypted_content1), "; Generated Key ===>", current_key)


def decrypter(encrypted_content2, decrypter_key):
  for item3 in encrypted_content2:
    item4 = list(root_key)[decrypter_key.index(item3)]
    content2.append(item4)
  print("Encrypted Text ===>", encrypted_content2, "; Decrypted / Original Text ===>",
        ''.join(content2), "; Key Used ===>", decrypter_key)

# Sample : Worked
# encrypter('appleberry')
# EI : jttiszshha
# Key : jznysdomuegiblqtchkvxpwraf
# Note : This was tested with only Ascii lowercase letters.

# Sample2 : Worked
# encrypter('Hello. This messaged is enc\'d. Thank you.')
# EI : ,;XXzfT|Oh=T);==:{;eTh=T;~ybefT|O:~UTQzVf
# Key : T:pye;\{OhAUX)~zI1}=iV5SBQN&kt"GF`,C?PJuH+.cn-|rMv(wL_smj#[gld>@029qKbxYRa8$fW/*%ED 6437Z<o^]!'

# Notes
# Remember to put the Encrypted Text and Keys within Single/Double Quotes (' / ") 
# Remember to put escape character (\) in case of either form of quote present in text.

# Does not work for Multiline Strings as of yet.

# Code Works...

# ----------------------------------------------------------------------------------------------------------

