# phantom-licensecheck

Check the open source licenses used in DJI Phantom 3 firmware, if any

# Motivation

Rumors are that OpenWrt is used in the Phantom firmware. If so, parts of the Phantom firmware would have to be provided by DJI in soure form. This project is to check the Phantom firmware for any open source code that might have such requirements.

# Hello world

```
binwalk ./P3X_FW_V01.02.0006.bin 2>&1 | grep Copyright
5592148       0x555454        Copyright string: " (c) 1996-2008 Express Logic Inc. * ThreadX ARM9/RVDS Version Gc. * ThreadX ARM9/RVDS Version G5.1.5.1 SN: 2923-115-1301 *"
35652448      0x2200360       Copyright string: " 2004-2014 Ambarella Corp.(PrSsg)"
43301892      0x294BC04       Copyright string: " (c) 1996-2014 Express Logic Inc. * ThreadX Cortex-A9/IAR Versic. * ThreadX Cortex-A9/IAR Version G5.6.5.1 SN: 3675-264-0901 *"
66914371      0x3FD0843       Copyright string: " (C) 2012 Free Software Foundation, Inc.ion, Inc."
66933671      0x3FD53A7       Copyright string: " (C) 2007-2012 Free Software Foundation, Inc.undation, Inc."
66934126      0x3FD556E       Copyright string: " (C) 2009-2012 Free Software Foundation, Inc.undation, Inc."
66934539      0x3FD570B       Copyright string: " (C) 2009-2012 Free Software Foundation, Inc.undation, Inc."
66935000      0x3FD58D8       Copyright string: " (C) 2009-2012 Free Software Foundation, Inc.undation, Inc."
66935454      0x3FD5A9E       Copyright string: " (C) 2007-2012 Free Software Foundation, Inc.undation, Inc."
66936775      0x3FD5FC7       Copyright string: " (C) 2007-2012 Free Software Foundation, Inc.undation, Inc."
66940059      0x3FD6C9B       Copyright string: " (C) 2009-2012 Free Software Foundation, Inc.undation, Inc."
66988409      0x3FE2979       Copyright string: " (C) 2005-2012 by Zack T Smith."
67389568      0x4044880       Copyright string: " 1991, 1992, 1994, 1998, 1999, 2002   William D. Norcott2002   William D. Norcott"
69442897      0x4239D51       Copyright string: " (c) 2004-2014, Jouni Malinen <j@w1.fi> and contributorsj@w1.fi> and contributors"
72243006      0x44E573E       Copyright string: " (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>ion, Inc. <http://fsf.org/>"
72246767      0x44E65EF       Copyright string: "" also means copyright-like laws that apply to other kinds ofs that apply to other kinds of"
72377128      0x4506328       Copyright string: " (C) 2012 Free Software Foundation, Inc.ion, Inc."
72405405      0x450D19D       Copyright string: " (C) 2007-2012 Free Software Foundation, Inc.undation, Inc."
72406981      0x450D7C5       Copyright string: " (C) 2007-2012 Free Software Foundation, Inc.undation, Inc."
72407475      0x450D9B3       Copyright string: " (C) 2007-2012 Free Software Foundation, Inc.undation, Inc."
72408139      0x450DC4B       Copyright string: " (C) 2011-2012 Free Software Foundation, Inc.undation, Inc."
72408870      0x450DF26       Copyright string: " (C) 2008-2012 Free Software Foundation, Inc.undation, Inc."
72409379      0x450E123       Copyright string: " (C) 2008-2009, 2011-2012 Free Software Foundation, Inc.Software Foundation, Inc."
72409827      0x450E2E3       Copyright string: " (C) 2010-2012 Free Software Foundation, Inc.undation, Inc."
72684088      0x4551238       Copyright string: " (C) 2001-2012 Charles Cazabon."
72708984      0x4557378       Copyright string: " (C) 2012, Thomas G. Lane, Guido Vollbedingo Vollbeding"
73801163      0x4661DCB       Copyright string: " (c) 2003-2014, Jouni Malinen <j@w1.fi> and contributorsj@w1.fi> and contributors"
74606570      0x47267EA       Copyright string: " (c) 2002-2014, Jouni Malinen <j@w1.fi> and contributorsj@w1.fi> and contributors"
75176721      0x47B1B11       Copyright string: " (C) 2001-2011 Alvaro Lopez Ortega.ega."
75251692      0x47C3FEC       Copyright string: " (C) 2001 - 2011 <a href="http://www.alobbs.com/">Alvaro Lopez //www.alobbs.com/">Alvaro Lopez Ortega</a> &lt;alvaro@alobbs.co"
75684779      0x482DBAB       Copyright string: " (c) 2000-2013 Simon KelleyyZDNLERKzowefnbvhdkqr:m:p:c:l:s:i:t:u:g:a:x:S:C:A:T:H:Q:I:B:F:G"
75746809      0x483CDF9       Copyright string: " (c) 2004-2014, Jouni Malinen <j@w1.fi> and contributorsj@w1.fi> and contributors"
76557967      0x4902E8F       Copyright string: " (C) 2013, Ambarella Inc."
78667783      0x4B06007       Copyright string: " (C) 2003-2010 Thomas Graf <tgraf@redhat.com>af@redhat.com>"
79068167      0x4B67C07       Copyright string: " 1995-2013 Jean-loup Gailly and Mark Adler  Mark Adler "
79268580      0x4B98AE4       Copyright string: " (C) 2012, Thomas G. Lane, Guido Vollbedingo Vollbeding"
85660269      0x51B126D       Copyright string: " (C) 2006 Free Software Foundation, Inc.ion, Inc."
89394065      0x5540B91       Copyright string: " (C) 2012 Free Software Foundation, Inc.ion, Inc."
89516078      0x555E82E       Copyright string: " (c) 2002 The OpenTSA Project.  All rights reserved. All rights reserved."
89540571      0x55647DB       Copyright string: " (C) 2001 Erik Andersen <andersen@codepoet.org>en@codepoet.org>"
92590284      0x584D0CC       Copyright string: " (c) 1996-2014 Express Logic Inc. * ThreadX Cortex-A9/IAR Versic. * ThreadX Cortex-A9/IAR Version G5.6.5.1 SN: 3675-264-0901 *"
```
