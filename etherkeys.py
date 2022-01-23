#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  15 07:27:37 2022

@author: Pete Laric / www.PeteLaric.com

Etherkeys is a novel key management solution that generates a table of strong
keys from a master passphrase.  The master passphrase is never given out
or used for anything else, so it cannot be compromised.  If a generated
key becomes compromised, it can simply be discarded and replaced with the
next one on the list.  Due to the one-way nature of cryptographic hash
functions, it is not feasible to deduce the master passphrase, or any of the
other keys, from a compromised key (assuming a strong passphrase is used).

The advantages of Etherkeys are multi-fold.  First, the ability to generate
all your passwords on the fly means you don't need to store them where they
could be lost or stolen.  When you need them, they can be summoned
instantaneously.  When you don't, they literally don't exist!  Second, it's
hard enough to remember a single strong password, much less a bunch of them.
This leads to people using weak passwords (e.g. "Apple123!"); using the same
password for multiple websites; or worse yet -- both.  Etherkeys solves this
by allowing you to use a unique, super-strong password for each and every
website -- one that you don't have to remember.

Example:

    passphrase: Let's Go Brandon
    output:
    #, preimage,           hash,                                                             key,                              usage
    0, Let's Go Brandon:0, f07ec2ecc15ae1696e94d75df2b7bbe0725caaff70a8234f263086d7c1f110d5, oSOkNi9xC4)lqDH8GkqDEoz7CM!)Npg*, PirateBay
    1, Let's Go Brandon:1, 952cfc76e18f49b86546180a08ca33b52f710e985ddde89d609eee36edf0e846, 5IAK9)1Et(oa8WPBLFe8l5gdoemSlog(, SilkRoad
    2, Let's Go Brandon:2, c23e9aed21cd6540220ae7e5a919d5438c6f34ee1beceee88092822178168d50, O!alxZt#yafdpp*^&DQmrkmgU2WxMm*8, AreaDenialWeapons
    etc.

Currently, the program is set to use the SHA-256 hash algorithm.  You can
confirm that hashes are being computed correctly from the command line
(Linux/Mac) using:

    echo -n "Let's Go Brandon:0" | shasum -a 256

Note that the "-n" is essential to suppress inclusion of a newline character in
the preimage, which leads to an incorrect hash.

SHA-256 hashes are 64 hexadecimal digits long.  Etherkeys converts each pair of
hex digits into a single key symbol (numerals: 0-9; letters a-z and A-Z; special
characters corresponding to the 10 numerical keys on a standard QWERTY
keyboard).  Therefore, passwords generated with Etherkeys are 32 characters
long by default.  They may, however, be truncated as needed.  The key_length
variable may be adjusted to any value between 1 and 32, and all generated keys
will be truncated to this length.

How secure is Etherkeys?  Well, if you use a very strong passphrase, and follow
best cybersecurity practices (run antivirus, don't download untrusted apps,
don't save passwords to cloud storage, etc.), it should be damn near
unbreakable.  Of course, it is always possible that in the distant future,
someone will come up with a way to crack SHA-256, but for now, it is considered
quite secure by the crypto community.  In fact, it is the backbone of many
cryptocurrencies like Bitcoin.  The number of possible 32-digit passwords, with
each digit having one of 72 different values, is 72^32.  That's 2.7 * 10^59.
If we assume that an adversary can guess and check one billion (10^9) passwords
per second, it would still take him ~8.56 * 10^42 years to crack a single
Etherkeys password, which is significantly longer than the observable universe
has existed.  Much more likely, he will prefer to simply hack into your computer
and steal your passphrase (e.g. through a keystroke logger), or he will try to
phish you into entering your passphrase into a fake version of Etherkeys.  For
this reason, it is extremely important to secure any device you use Etherkeys
on, and to always verify the source before downloading it.

If you find Etherkeys useful or have any ideas for ways it could be improved,
I would love to hear from you:

    PeteLaric at protonmail dot com

Cheers,
~ Pete
"""

# libraries
import hashlib

# globals
num_keys = 100 #how many keys to generate
key_length = 10 #[1,32] -- truncate generated keys to this length
conversion_key = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
conversion_key_length = len(conversion_key)
separator = "," #for separating columns in printed output
show_preimage = False #mostly for diagnostics; keep False for security reasons
show_hash = False #also mostly for diagnostics


# converts a hexadecimal cryptographic hash into a password string (0-9,a-f,A-F,symbols)
def hash2pass(my_hash):
    hash_length = len(my_hash)
    half_length = int(hash_length / 2)
    my_pass = ""
    for j in range(half_length):
        # map each pair of hex digits to an integer in the range [0,255]
        first_digit = my_hash[j*2] #extract first hex digit from hash (most significant digit)
        second_digit = my_hash[(j*2)+1] #extract second hex digit from hash (least significant digit)
        dec = int(first_digit + second_digit, 16) #convert to decimal (integer)
        # convert decimal value to password value
        key_index = dec % conversion_key_length
        p = conversion_key[key_index]
        #print(p, end="")
        my_pass += p #append password character to password string
    return my_pass


passphrase = input("passphrase: ")
print()

# show header row
print("#" + separator, end="")
if (show_preimage):
    print("preimage" + separator, end="")
if (show_hash):
    print("hash" + separator, end="")
print("key" + separator, end="")
print("usage")

# show keys
for i in range(num_keys):
    preimage = passphrase
    preimage = preimage.rstrip() #strip off newline chars
    preimage += ":" + str(i) #append hash index
    print(i, end=separator) #print hash index
    if (show_preimage):
        print(preimage, end=separator) #print preimage

    preimage = preimage.encode('utf-8') #transcode to UTF-8 (required in Python3)
    m = hashlib.sha256() #select SHA-256 algorithm
    m.update(preimage) #take hash of preimage
    my_hash = m.hexdigest()

    if (show_hash):
        print(my_hash, end=separator) #print hash

    # now convert hex hash to password-style string
    my_pass = hash2pass(my_hash)
    my_pass = my_pass[0:key_length] #truncate to desired length
    print(my_pass, end="")

    print(separator + "N/A")
