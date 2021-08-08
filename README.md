# etherkeys
A novel password management program that generates keys using cryptographic hashes of a master key.

	etherkeys.c
	(c) 2021-08-07 Pete Laric
	http://www.PeteLaric.com
	
	A simple program that deterministically generates a table of keys from a single user-provided master key.
	The advantage of etherkeys is, you don't have to store all your passwords where they could get lost or stolen.
	When you need them, they appear.
	When you don't need them, they disappear.  They literally don't exist.
	Never use your master password for anything else, and it shouldn't be possible for anyone to figure out what it is, ever.
	If one generated key becomes compromised, simply stop using it.  Simple.  You can generate as many as you need.
	
	Enjoy this free software, and please consider sending a donation to support my work!
	
	Email:
	p e t e l a r i c
	a t p r o t o n m
	a i l d o t c o m
	
	Bitcoin:
	1EExevPZkgjoRFEbQzTFLpAoyDpwAdeQXw
	
	
	COMPILATION INSTRUCTIONS:
	
	Under Linux, use GCC in Terminal:
	
		gcc -g -Wall etherkeys.c -lm -o etherkeys
	
	
	USAGE:
	
		./etherkeys ["PASSPHRASE"]
	
	Quotation marks are optional for one-word keys, but necessary for multi-word passphrases if spaces are used between words.
