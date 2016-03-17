# Structure of firmware package file

### Filenames and drone types

Firmware package files can by found at the website of DJI, at the support page of each Phantom 3 drone. Only some recent firmware files are online, there is not yet a repository for older firmware files. 

DJI uses the format `<model code>_FW_V<version>.<subversion>.<subversion2>.bin` for firmware package files and only such files are used for update. On some occasion, beta files are marked `..._beta.bin`. , 

Firmware package files analyzed so far are:

* P3X_FW_V01.07.0048_beta.bin (0.8MB)
* P3X_FW_V01.06.0040.bin (65MB)
* P3X_FW_V01.05.0030.bin (65MB)
* P3X_FW_V01.03.0020.bin (95MB)
* P3XW_FW_V01.03.0021.bin (66MB)
* P3S_FW_V01.07.0048_beta.bin (0.8MB)
* P3S_FW_V01.06.0040.bin (62MB)
* P3S_FW_V01.05.0030.bin (62MB)
* P3S_FW_V01.03.0020.bin (92MB)
* P3C_FW_V01.04.0051.bin (66MB)

### General structure

Every firmware package file consists of a file header, a seek table with one entry per firmware module, a checksum and finaly a number of firmware modules corresponding to different sub systems of the drone. 

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

Furthermore, there is a 2 byte checksum after the last seek table entry. The offset value has to be calculated as 52 * 'number of rows'

```
074 - 075 + off	checksum of header + seek table, typ unknown
```

### Seek table

The offset value has to be calculated as 52 * 'row number'. 

```
040 - 073 + off	seek table (52 byte * number of rows)
					00 - 00	 1 byte firmware module type 
					01 - 01	 1 byte special coding - either '10' = DJI or '00' = none
					02 - 03	 2 byte <?> mostly 01 00
					04 - 07	 4 byte firmware module version (byte wise from right to left)
					08 - 0B	 4 byte absolut position of firmware module within firmware package file
					0C - 0F	 4 byte length of firmware module
					10 - 13	 4 byte length of firmware module (repeated <?>)
					14 - 23	16 byte MD5 hash of firmware module
					24 - 33	16 byte <?> possibly other hash
```

The different firmware module types are described in this document (http://www.github.com/)

### Open qustions

- [ ] For what reason is the file length information repeated within the seek table?
- [ ] What is the function of the second "hash" type field within the seek table?
- [ ] How is the 2 byte checksum composed?
- [ ] How is the firmware package file version composed?
- [ ] Why are firmware mosule subversion somtimes slightly different from what is shown at upgrade logs?

### Tools

* A simple python script is included to split every firmware package file into separate firmware modules. Syntax: `dji_split.py <filename.bin>`
