/*
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
	
		./etherkeys ["PASSPHRASE"] [TABLE_SIZE]
	
	Quotation marks are optional for one-word keys, but necessary for multi-word passphrases if spaces are used between words.
	TABLE_SIZE is simply the number of keys you want to generate.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 	     1000
#define SHA_VERSION 	     1     // acceptable values include 1, 256, 512
#define DEFAULT_TABLE_SIZE  10    // number of keys to generate


void get_hash(char *key, int i)
{

	//printf("%i:\n", i);
	
	char *cmd = malloc(BUFFER_SIZE * sizeof(char));
	
	sprintf(cmd, "echo \"%s:%i\" | shasum -a %i", key, i, SHA_VERSION);
	
	//printf("cmd: %s\n", cmd); //diagnostic
	///////printf("%s:%i\n", key, i); //remmed as of 2021-10-11
	system(cmd);
	///////printf("\n");//remmed as of 2021-10-11
	
	free(cmd);
}


int main(int argc, char *argv[])
{
	// diagnostic
	//printf("argc: %i\n", argc);
	//printf("argv[1]: %s\n", argv[1]);
	
	char *master_key = argv[1];
	//printf("master_key: %s\n", master_key);
	
	if (argc <= 1)
	{
		printf("Usage:\n\n");
		printf("\tetherkeys [\"PASSPHRASE\"] [TABLE_SIZE]\n\n");
		printf("Quotation marks are optional for one-word keys, but necessary for\n");
		printf("multi-word passphrases if spaces are used between words.\n\n");
		return 1;
	}
	
	int TABLE_SIZE = DEFAULT_TABLE_SIZE;
	if (argc >= 3)
	{
		TABLE_SIZE = atoi(argv[2]);
	}
	
	//printf("\n");
	
	//system("shasum /dev/null"); //da39a3ee5e6b4b0d3255bfef95601890afd80709
	
	int i = 0;
	
	for (i = 0; i < TABLE_SIZE; i++)
	{
		get_hash(master_key, i);
	}

	
	return 0;
}

