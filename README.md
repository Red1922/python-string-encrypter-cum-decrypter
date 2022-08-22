# python-string-encrypter-cum-decrypter
PSED is an Encrypter as well as a Decrypter tool program which generates a unique key and uses it to Encrypt a message or it can use an existing key to decrypt a message that had been encrypted using the said key. Each key has a uniqueness of being 1 in 69! possible keys, in more exact terms, 1 in 1.71122452428e+98 keys. PSED is currently only a cli tool and only supports the Latin Alphabets, Numeric Digits 0-9 and common punctuation symbols. This is still work in progress. Contributions and Pull Requests will be appreciated.

# Explanation of Mechanism

Example:
word to be encrypted = `Apple`

Root Key = `ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz` (I am only taking letters for now)

Function `generate_key()` will Generate a Key by shuffling the root key --> `ACEGIKMOQSUWYBDFHJLNPRTVXZacegikmoqsuwybdfhjlnprtvxz`


Here the `encrypter(content1)` function will take an input in text(string) which has been assigned the variable `content1`, here `content1 = "Apple"`

The function will then take each letter of `Apple` and take its index position from the root key, for example `'A' lies in index '0' of Root Key while 'p' lies in index '41' of root key and so on.` 
Using these indexes, the function will then take out the letters in those index positions from our generated key. `Here, index '0' still has 'A' while index '41' has 'u' and so on.` 
The function will now take those letters from the generated key and append it to an empty list we had created before hand, say `list1`. So after the letter swapping is complete, `list1 = "Auu@#"` (I did not look for the other letters as it is a tedious process)
Then we will convert the list to a string and print it.

Now your message is encrypted.


To decrypt it. You will need to run function `decrypter(content2,gen_key)` which will accept your decrypted content stored as `content2`, may also be equal to `content1` and your generated key that you used to encrypt the original message. 

The process of decryption is just the same but opposite in nature. We will take the characters in our encrypted content, find their index position in the generated key, use that index to find the letter in that position in the root key, take that letter from the root key and append it to empty list, here `list2` which after the entire process of swapping characters should be `list2 = "Apple"`.
Then we will convert this list to a string and print it.

Now your encrypted message has been decrypted to its originality.

The whole code utilizes numeric characters as well as most punctuation symbols like `.,;:'"/><][{}()\|-_+=*&%$#@!^~` maybe add or remove a few

For the time being it can only encrypt and of course decrypt, Latin characters. That is, only those characters present in the root key
and also the space character -->` `<--
