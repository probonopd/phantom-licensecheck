# Structure of firmware package file

### Filenames and drone types

### General structure

### Header

```
000 - 003f		header (64 byte)
					00 - 05	 6 byte unique identifier - '78 56 34 12 01 00'
					06 - 07 	 2 byte pointer to first firmware module
					08 - 09 	 2 byte <?>
					0A - 0B	 2 byte firmware version code 
					0C - 1B	16 byte manufacturer string - 'DJI' followed by '00'
					1D - 2B	16 byte model string - 'P3X', 'P3S', 'P3C' or 'P3XS' followed by '00' 
					2C - 2D	 2 byte number of rows (52 byte each) in seek table
					2E - 31	 4 byte <?>
					32 - 35	 4 byte <?>
					36 - 3F	10 byte <?> moslty '00'
```

Furthermore, there is a 2 byte checksum after the last seek table entry. The offset value has to be calculated as 52 * <number of rows>

```
074 - 075 + off	checksum of header + seek table, typ unknown
```

### Seek Table

The offset value has to be calculated as 52 * <row number>. 

```
040 - 073 + off	seek table (52 byte * number of rows)
					00 - 00	 1 byte firmware module type 
					01 - 01	 1 byte special coding - either '10' = DJI or '00' = none
					02 - 03	 2 byte <?> mostly 01 00
					04 - 07	 4 byte absolut position of firmware module within firmware package file
					08 - 1B	 4 byte length of firmware module
					1C - 1F	 4 byte length of firmware module (repeated <?>)
					20 - 2F	16 byte MD5 hash of firmware module
					30 - 3F	16 byte <?> possibly other hash
```

The different firmware module types are described in this document (http://www.github.com/)

### Open qustions

- [ ] For what reason is the file length information repeated two times within the seek table?
- [ ] What is the function of the second "hash" type field within the seek table?
- [ ] How is the 2 b`yte checksum composed?
- [ ] What is the function of 

### Tools

* A simple python script is included to split every firmware package file into separate firmware modules. (http://www.github.com/). Syntax: `dji_split <filename.bin>`
