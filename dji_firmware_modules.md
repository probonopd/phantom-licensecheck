#  Description of DJI Phantom 3 Firmware modules

### Overview of firmware modules

```
Typ 	O.S.L.	Encrypt	Function
0100	yes		  no		  (checked)  Camera subsystem, provided by
0400	unclear	no		  (possibly) Gimbal
0410	unclear	dji		  (possibly) Gimbal
0500	unclear	no		  (possibly) Battery Firmware
0700	yes		  no		  (possibly) Range extender, based on U-Boot / Open WRT
0800	unclear	openssl	(unknown) 
0900	unclear	no		  (guessed)  Image transmitter
0b00	unclear	no		  (guessed)  Intelligent flight battery
0c00	unclear	no		  (possibly) ESC motor controller 1. Unencrypted version. See also 0C, 2C, 4C, 6C
0c10	unclear	dji		  (possibly) ESC motor controller 1. Encrypted version. See also 0C, 2C, 4C, 6C
0d00	unclear	openssl	(unknown)
0e00	unclear	no		  (possibly) Remote controller	
0f00	no		  no		  (checked)  EZ-USB FX2 Controller	
1000	no		  no		  (checked)  EZ-USB FX2 Controller (different Version)
1100	no		  no		  (checked)  MPU6050 Gyroscope Board
1300	unclear lzma	  (unknown)
1400	unclear	lzma	  (unknown)	
1b00	yes		  no		  (checked)  Range extender, based on U-Boot / Open WRT	
2100	no		  no		  (checked)  Firmware package updater. Based on ThreadX
2b00	no		  no		  (possibly) Battery Firmware	
2c00	unclear	no		  (possibly) ESC motor controller 2. Unencrypted version. See also 0C, 2C, 4C, 6C
2c10	unclear	dji		  (possibly) ESC motor controller 2. Encrypted version. See also 0C, 2C, 4C, 6C
3000	no		  no		  (possibly) GL300B Remote controller firmware. Based on ThreadX	
3100	unclear	no		  (unknown)	
3400	unclear	unclear	(unknown)		
4c00	unclear	no		  (possibly) ESC motor controller 3. Unencrypted version. See also 0C, 2C, 4C, 6C
4c10	unclear	dji		  (possibly) ESC motor controller 3. Encrypted version. See also 0C, 2C, 4C, 6C
5400	unclear	unclear	(unknown)  	
6c00	unclear	no		  (possibly) ESC motor controller 4. Unencrypted version. See also 0C, 2C, 4C, 6C
6c10	unclear	dji		  (possibly) ESC motor controller 4. Encrypted version. See also 0C, 2C, 4C, 6C
a310	unclear	dji		  (unknown)	
c310	unclear	dji		  (checked)  NAZA main flight controller firmware

Note: O.S.L.=Open Source Licensed material; Encrypt dji=unknown proprietary encryption by dji
```

Other missing hardware components:

- [ ] GPS-Glonass vs. GPS-only module
- [ ] Vision Positioning System

### Firmware modules present in firmware 

A a total of 13 firmware packages have been analyzed. The following table indicates the relevance of each firmware module for different drone models. 

```
Typ	  	P3C	P3S	P3X	P3W	I1	total 
0100	  1	  3	  3	  1	  3	  11
0400					          2	   2
0410	  1	  3	  3	  1	  1	   9
0500					          3	   3
0700	  1			      1		     2
0800			  3		3	           6
0900	  1	  3	  3	  1	  3	  11
0b00	  1	  3	  3	  1	  3	  11
0c00	  1			      1		     2
0c10		    3	  3		    3	   9
0d00		    1	  1		    1	   3
0e00	  1	  1	  1	  1	  1	   5
0f00		    3	  3		    3	   9
1000		    1	  1		    1	   3
1100		    3	  3	  1	  3	  10
1300		    3	  3		    3	   9
1400		    1	  1		    1	   3
1b00	   1			    1		     2
2100	   1	3	  3	  1	  3	  11
2b00				        1		     1
2c00	   1			    1		     2
2c10		    3	  3		    3	   9
3000		    1	  1			       2
3100		    3	  3	  1	  3	  10
3400		    1	  1		    1	   3
4c00	   1			    1		     2
4c10		    3	  3		    3	   9
5400		    1	  1			       2
6c00	   1			    1		     2
6c10		    3	  3		    3	   9
a310	   1	3	  3	  1	  3	  11
c310	   1	4	  4	  1	  3	  13

Note: P3W=P3XW, I1=PW610 (Inspire 1)
```

### Module by modulue analysis

#### 0100 Camera Subsystem

```
56.618.460	0100	V1.26.16.219	P3X		V01.06.0040.bin
56.618.460	0100	V1.26.16.219	P3X		V01.05.0030.bin
56.869.164	0100	V1.23.13.91		P3X		V01.03.0020.bin
56.766.764	0100	V1.22.15.255	P3S		V01.06.0040.bin
56.766.764	0100	V1.22.15.255	P3S		V01.05.0030.bin
56.762.668	0100	V1.20.13.91		P3S		V01.03.0020.bin
56.395.228	0100	V1.13.16.216	P3C		V01.04.0051.bin
56.651.228	0100	V1.1.17.201		P3XW	V01.03.0021.bin
```

##### Findings

This is the longest firmware module file with a size of >56MB and contains references to Ambarella. 
According to this article, the Ambarella CEO noted that DJI "brought to market its Phantom 3 drones, 
both powered by Ambarella's A9 camera systems-on-chip". This fits to the fact that strings 
like autobuild_A9_Ambalink_AR6004/ambalink_sdk/host/usr/arm-buildroot-linux-gnueabi are found in the 
Phantom 3 Advanced firmware. According to the Product Brief, the Ambarella A9 has two ARM® CORTEX-A9 and 
one ARM® 11 cores and can do 4K. The camera subsystem is therefor the most powerful hardware module present 
in in the drone.

The firmware module file consists of multiple parts, probably different partitions, including a UBI partition. 
The main kernel is Linux 3.8.0 according to STRINGS. There are references to minix and ambafs file systems. There 
are at least 2 MySQL Database files.

In the last fifth of the file, some clear text informations about an unknown communication interface are exposed, 
including private keys, wpa passwords, etc.

#### 0400 Gimbal
#### 0410 Gimbal

```
93.696	0410	V1.41.0.0	P3S		V01.06.0040.bin
93.696	0410	V1.41.0.0	P3X		V01.06.0040.bin
93.696	0410	V1.41.0.0	P3S		V01.05.0030.bin
93.696	0410	V1.41.0.0	P3X		V01.05.0030.bin
93.696	0410	V1.41.0.0	P3C		V01.04.0051.bin
93.696	0410	V1.41.0.0	P3XW	V01.03.0021.bin
89.344	0410	V1.40.0.0	P3S		V01.03.0020.bin
89.344	0410	V1.40.0.0	P3X		V01.03.0020.bin
```

##### Findings

Although most files are dji encrypted, the later versions for Inspire 1 are present in an uncoded format. A reference 
to "HP310" in this file shows its connection to the Zenmuse X3 gimbal & camera. 

#### 0500 Battery

##### Findings

His firmware module file only exists in Inspire 1 files.

#### 0700 Range extender
#### 1b00 Range extender

```
3.997.732	0700	V1.0.9.42	P3XW	V01.03.0021.bin
4.180.228	0700	V1.0.9.14	P3C		V01.04.0051.bin
3.997.732	1b00	V1.0.9.42	P3XW	V01.03.0021.bin
4.180.228	1b00	V1.0.9.14	P3C		V01.04.0051.bin
```

##### Findings

This firmware module only exists in P3XW and P3C models not equipped with lightbridge. The range extender software 
is clearly based on a MIPS processor, and runs OpenWRT form a UBOOT partition.

#### 0800 unknown

```
3.363.336	0800	V0.13.0.7	P3X		V01.06.0040.bin
3.363.336	0800	V0.13.0.7	P3X		V01.05.0030.bin
3.344.952	0800	V0.12.0.4	P3X		V01.03.0020.bin
```

##### Findings

This firmware module only exists on P3X an I1 firmware packages, Its function is yet unknown. The firmware module file includes 
fingerprints of a salted ssl encryption. 

#### 0900 Image transmitter

```
81.284	0900	V2.13.0.0	P3S		V01.06.0040.bin
81.284	0900	V2.13.0.0	P3X		V01.06.0040.bin
81.284	0900	V2.13.0.0	P3S		V01.05.0030.bin
81.284	0900	V2.13.0.0	P3X		V01.05.0030.bin
68.536	0900	V1.7.0.3	P3S		V01.03.0020.bin
68.536	0900	V1.7.0.3	P3X		V01.03.0020.bin
60.224	0900	V0.1.1.0	P3C		V01.04.0051.bin
53.488	0900	V0.1.0.12	P3XW	V01.03.0021.bin
```

##### Findings

In the P3C and P3XW versions, this file also contains STRINGS for WLAN connectivity.

#### 0b00 Intelligent flight battery

```
18.348	0b00	V1.8.0.0	P3C		V01.04.0051.bin
18.348	0b00	V1.8.0.0	P3XW	V01.03.0021.bin
19.140	0b00	V1.7.15.1	P3S		V01.06.0040.bin
19.140	0b00	V1.7.15.1	P3X		V01.06.0040.bin
19.008	0b00	V1.7.0.0	P3S		V01.05.0030.bin
19.008	0b00	V1.7.0.0	P3X		V01.05.0030.bin
19.008	0b00	V1.7.0.0	P3S		V01.03.0020.bin
19.008	0b00	V1.7.0.0	P3X		V01.03.0020.bin
```

##### Findings

Present in almost any firmware package, the reference BQ76930 suggests, that this firmware 
module is used for the Texas Instruments BQ76930 Battery Management chip. (http://www.ti.com/product/BQ76930)

#### 0c00 2c00 4c00 6c00 ESC motor controller
#### 0c10 2c10 4c10 6c10 ESC motor controller

```
 3.556	0c00	V5.9.0.0	P3C		V01.04.0051.bin
 3.556	0c00	V5.9.0.0	P3XW	V01.03.0021.bin
41.728	0c10	V1.8.0.0	P3S		V01.03.0020.bin
41.728	0c10	V1.8.0.0	P3X		V01.03.0020.bin
42.496	0c10	V1.10.0.0	P3S		V01.06.0040.bin
42.496	0c10	V1.10.0.0	P3X		V01.06.0040.bin
42.496	0c10	V1.10.0.0	P3S		V01.05.0030.bin
42.496	0c10	V1.10.0.0	P3X		V01.05.0030.bin
 3.556	2c00	V5.9.0.0	P3C		V01.04.0051.bin
 3.556	2c00	V5.9.0.0	P3XW	V01.03.0021.bin
41.728	2c10	V1.8.0.0	P3S		V01.03.0020.bin
41.728	2c10	V1.8.0.0	P3X		V01.03.0020.bin
42.496	2c10	V1.10.0.0	P3S		V01.06.0040.bin
42.496	2c10	V1.10.0.0	P3X		V01.06.0040.bin
42.496	2c10	V1.10.0.0	P3S		V01.05.0030.bin
42.496	2c10	V1.10.0.0	P3X		V01.05.0030.bin
 3.556	4c00	V5.9.0.0	P3C		V01.04.0051.bin
 3.556	4c00	V5.9.0.0	P3XW	V01.03.0021.bin
41.728	4c10	V1.8.0.0	P3S		V01.03.0020.bin
41.728	4c10	V1.8.0.0	P3X		V01.03.0020.bin
42.496	4c10	V1.10.0.0	P3S		V01.06.0040.bin
42.496	4c10	V1.10.0.0	P3X		V01.06.0040.bin
42.496	4c10	V1.10.0.0	P3S		V01.05.0030.bin
42.496	4c10	V1.10.0.0	P3X		V01.05.0030.bin
 3.556	6c00	V5.9.0.0	P3C		V01.04.0051.bin
 3.556	6c00	V5.9.0.0	P3XW	V01.03.0021.bin
41.728	6c10	V1.8.0.0	P3S		V01.03.0020.bin
41.728	6c10	V1.8.0.0	P3X		V01.03.0020.bin
42.496	6c10	V1.10.0.0	P3S		V01.06.0040.bin
42.496	6c10	V1.10.0.0	P3X		V01.06.0040.bin
42.496	6c10	V1.10.0.0	P3S		V01.05.0030.bin
42.496	6c10	V1.10.0.0	P3X		V01.05.0030.bin
```

##### Findings

The ESC controller for the (newer) P3C and P3XW models is unencrypted and much shorter compared to the P3S and P3X version. 

#### 0d00 unknown

```
4.368.784	0d00	V2.18.0.1	P3S		V01.03.0020.bin
4.368.784	0d00	V2.18.0.1	P3X		V01.03.0020.bin
```

##### Findings

The file is encoded by salted SSL. This file does not exist in P3C and P3XW versions. Possibly Vision positioning system (wild guess)?

#### 0e00 Remote controller

```
125.512	0e00	V4.9.3.0	P3S		V01.03.0020.bin
125.512	0e00	V4.9.3.0	P3X		V01.03.0020.bin
 56.104	0e00	V4.1.1.5	P3XW	V01.03.0021.bin
 62.144	0e00	V4.1.1.0	P3C		V01.04.0051.bin
```

##### Findings

Only some firmware packages include the remote controller update. STRINGS within the P3C and P3XW modules include references to Wifi settings. 
These settings are missing in P3X an P3S firmware files.  

#### 0f00 EZ-USB FX2 Controller
#### 1000 EZ-USB FX2 Controller

```
2.680	0f00	V1.1.2.0	P3S		V01.06.0040.bin
2.680	0f00	V1.1.2.0	P3X		V01.06.0040.bin
2.680	0f00	V1.1.2.0	P3S		V01.05.0030.bin
2.680	0f00	V1.1.2.0	P3X		V01.05.0030.bin
2.680	0f00	V1.1.2.0	P3S		V01.03.0020.bin
2.680	0f00	V1.1.2.0	P3X		V01.03.0020.bin
2.750	1000	V1.3.1.0	P3S		V01.03.0020.bin
2.750	1000	V1.3.1.0	P3X		V01.03.0020.bin
```

##### Findings

Very small firmware module corresponding to the Cypress EZ-USB FX2 Microcontroller (http://www.cypress.com/products/ez-usb-fx2lp). P3X and P3S
might have a second USB unit (1000).

#### 0100 MPU6050 gyroscope board

```
77.876	1100	V1.1.1.7	P3S		V01.06.0040.bin
77.876	1100	V1.1.1.7	P3X		V01.06.0040.bin
77.876	1100	V1.1.1.7	P3S		V01.05.0030.bin
77.876	1100	V1.1.1.7	P3X		V01.05.0030.bin
77.876	1100	V1.1.1.7	P3XW	V01.03.0021.bin
77.876	1100	V1.1.1.7	P3S		V01.03.0020.bin
77.876	1100	V1.1.1.7	P3X		V01.03.0020.bin
```

##### Findings

The Invensense MPU6050 is a 6-axis Gyro+Accelerometer one Chip solution with I2C interface. (http://www.invensense.com/products/motion-tracking/6-axis/mpu-6050/).
STRINGS indicate that this is the corresponding firmware module. 

#### 1300 unknown

```
4.194.304	1300	V1.0.8.96	P3S		V01.06.0040.bin
4.194.304	1300	V1.0.8.96	P3X		V01.06.0040.bin
4.194.304	1300	V1.0.8.96	P3S		V01.05.0030.bin
4.194.304	1300	V1.0.8.96	P3X		V01.05.0030.bin
4.194.304	1300	V1.0.8.96	P3S		V01.03.0020.bin
4.194.304	1300	V1.0.8.96	P3X		V01.03.0020.bin
```

##### Findings

This firmware module is exactly 1/2 the Size of 1400, 3400 and 5400. The structure is multiple tables, then a data area probably lzma coded. 
Finally, a large part of file is empty.

#### 1400 unknown
#### 5400 unknown

```
8.388.608	1400	V1.0.8.59	P3S		V01.03.0020.bin
8.388.608	1400	V1.0.8.59	P3X		V01.03.0020.bin
8.388.608	5400	V1.2.8.61	P3S		V01.03.0020.bin
8.388.608	5400	V1.2.8.61	P3X		V01.03.0020.bin
```

##### Findings

In P3S and P3X, these firmware modules come in tandem. In I1, only 1400 is present. The structure is multiple tables, then a data area probably lzma coded. 
Finally, a large part of file is empty.

#### 2100 Firmware package updater

```
412.780	2100	V1.26.16.219	P3X		V01.06.0040.bin
412.780	2100	V1.26.16.219	P3X		V01.05.0030.bin
412.780	2100	V1.23.13.91		P3X		V01.03.0020.bin
412.780	2100	V1.22.15.255	P3S		V01.06.0040.bin
412.780	2100	V1.22.15.255	P3S		V01.05.0030.bin
412.780	2100	V1.20.13.91		P3S		V01.03.0020.bin
412.780	2100	V1.13.16.216	P3C		V01.04.0051.bin
412.780	2100	V1.1.17.201		P3XW	V01.03.0021.bin
```

##### Findings

This firmware module corresponds to the Firmware updater. The version number is identical with the Camera subsystem, 
probabely the updater is loaded before/alternatively to the Camera hardware as it makes use of the CF card. The Firmware uses
the proprietary ThreadX mini Unix distribution licensed in the name of DJI.

With a high probability, this module contains all code for creating the firmware checksums, and also decrypts all "dji" 
encrypted firmware modules (as encrypted / cleartext versions of the same firmware module exist in different packages (i.e. 0c00 and 0c10,
0400 and 0410). Understanding this firmware module could be essential for a deeper understanding of other firmware modules.

#### 2b00 Battery firmware	

```
21.978	2b00	V2.0.0.32	P3XW	V01.03.0021.bin
```

##### Findings

Only present in one firmware package, it includes PHANTOM3_BAT and BATTERY strings.

#### 3000 GL300B Remote controller firmware

```
184.036	3000	V2.0.0.2	P3S		V01.03.0020.bin
184.036	3000	V2.0.0.2	P3X		V01.03.0020.bin
```

##### Findings

Only present in P3S and P3X. The firmware file is based on Express Logic ThreadX OS running on ARM9 processor.
The string GL300B indicates, that this is the remote controller firmware.

#### 3100 unknown

```
25.908	3100	V1.0.2.7	P3S		V01.06.0040.bin
25.908	3100	V1.0.2.7	P3X		V01.06.0040.bin
25.908	3100	V1.0.2.7	P3S		V01.05.0030.bin
25.908	3100	V1.0.2.7	P3X		V01.05.0030.bin
25.908	3100	V1.0.2.7	P3XW	V01.03.0021.bin
25.908	3100	V1.0.2.7	P3S		V01.03.0020.bin
25.908	3100	V1.0.2.7	P3X		V01.03.0020.bin
```

##### Findings

All but one early version of I2 files are identical. A STRING "System initialized" can be found.

#### 3400 unknown

```
8.388.608	3400	V1.1.8.59	P3S		V01.03.0020.bin
8.388.608	3400	V1.1.8.59	P3X		V01.03.0020.bin
```

##### Findings

The structure is similar to 1400 and 5400, it multiple tables, then a data area probably lzma coded. 
Finally, a large part of file is empty.

#### a310 unknown

```
43.776	a310	V34.2.0.9	P3S		V01.06.0040.bin
43.776	a310	V34.2.0.9	P3X		V01.06.0040.bin
43.776	a310	V34.2.0.9	P3S		V01.05.0030.bin
43.776	a310	V34.2.0.9	P3X		V01.05.0030.bin
43.776	a310	V34.2.0.9	P3C		V01.04.0051.bin
43.776	a310	V34.2.0.9	P3XW	V01.03.0021.bin
43.776	a310	V34.2.0.9	P3S		V01.03.0020.bin
43.776	a310	V34.2.0.9	P3X		V01.03.0020.bin
```

##### Findings

This file is identical for within all P3 firmware packages, and identical within all I1 firmware packages. 

#### c310 NAZA main flight controller firmware

```
824.320	c310	V2.4.20.10	P3S		V01.07.0048_beta.bin
824.320	c310	V2.4.20.10	P3X		V01.07.0048_beta.bin
830.976	c310	V2.4.20.10	P3C		V01.04.0051.bin
831.232	c310	V2.4.20.10	P3XW	V01.03.0021.bin
786.432	c310	V2.4.10.7	P3S		V01.06.0040.bin
786.432	c310	V2.4.10.7	P3X		V01.06.0040.bin
781.568	c310	V2.4.0.5	P3S		V01.05.0030.bin
781.568	c310	V2.4.0.5	P3X		V01.05.0030.bin
712.704	c310	V2.2.6.19	P3S		V01.03.0020.bin
712.704	c310	V2.2.6.19	P3X		V01.03.0020.bin
```

##### Findings

As this firmware module file is the only one present in the _beta firmware packages for P3X and P3S,
it is clear that this is corresponding to the main flight controller. It is certain that 
the flight restriction tables are also part of this file. 

### Results

tbc
