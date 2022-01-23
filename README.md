# etherkeys
A novel password management program that generates keys using cryptographic
hashes of a master passphrase.

Demo video: [IN PROGRESS...]  Here's an old one: https://youtu.be/WlUymjBRrZo

	etherkeys.py
	(c) 2022-01-23 Pete Laric
	http://www.PeteLaric.com

	A simple program that deterministically generates a table of keys from a
	single user-provided master passphrase.

	The advantage of Etherkeys is, you don't have to store all your passwords
	where they could get lost or stolen.  When you need them, they appear.  When
	you don't need them, they disappear.  They literally don't exist.

	Never use your master password for anything else, and it shouldn't be possible
	for anyone to figure out what it is, ever.  If one generated key becomes
	compromised, just stop using it.  Simple.  You can generate as many as you
	need.

	Enjoy this free software, and please consider sending a donation to support my
	work!

	Email:
	p e t e l a r i c
	a t p r o t o n m
	a i l d o t c o m

	Bitcoin:
	1EExevPZkgjoRFEbQzTFLpAoyDpwAdeQXw


	HOW TO USE:

	Under Linux or MacOS terminal, type the following:

		python3 etherkeys.py

	You will be prompted for your master passphrase.  When you hit ENTER, a table
	of keys will be generated for you.  You can copy-paste this table into a .CSV
	file and open it with a spreadsheet editor like LibreOffice Calc.  Or you can
	create the CSV automatically using an output redirect:

		echo "my passphrase" | python3 etherkeys.py > my_keys.csv

	Use the spreadsheet to keep track of which keys you use for what.  For added
	security, you can delete the column containing the actual keys, and instead
	retain only those corresponding to the key number and the usage.  This will
	necessitate running Etherkeys every time you want to retrieve a key, but it
	will also mean that your keys won't be sitting around on your hard drive for
	nosy maids to discover.

	Remember: never use your master passphrase for anything else!  It is only to
	be used for generating your key table.  If you adhere to this one rule, you
	will enjoy the utmost key management security.


	FAQ:

	Q: Can Etherkeys be used under Windows?
	A: Yes, but Windows is insecure and should not be used.  Fortunately, Linux
	can be installed on nearly any Windows computer.  I recommend the Ubuntu
	distribution.

	Q: Can Etherkeys be used on my phone?
	A: Yes, there are Python interpreters for mobile devices, and these should
	run Etherkeys without any difficulty.  However, phones are not very secure in
	my opinion, so please exercise caution.

	Q: When will you make a version with a nice GUI interface?
	A: If there is enough interest in the project, I will probably do this.  I
	made this tool primarily for myself, and I don't need a GUI for anything.

	Q: How do I know it's secure?
	A: It's open source, so you can examine the source code yourself.  It's a very
	simple program.  As for the SHA-256 algorithm, it underpins many modern
	technologies including Bitcoin, so if it's not secure, we have bigger
	problems.

	Q: I want "X" feature!
	A: If you think others might be interested, drop me a line and maybe I'll
	implement it.  Or, you can add it yourself.  That's the beauty of open source!
