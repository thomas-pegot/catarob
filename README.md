Analyz Granulometry from Images based on segmentation

Release 0.5

=============================================
ANALYZ
=============================================


Summary
-------

Provides ...


Links
-----


-----------------------------------------------
Build instructions (all platforms)
----------------------------------------------

Compilation is ensured by Python distutils tools.

You will need the following tools :

 * Python version 2.6 or later with the distutils package.
 * Swig version 1.3.33 or later.
 * GCC version 4.3.0 or later (or its windows version MingW32)
 * Standard C libraries
 
 * Under Windows, you might choose Microsoft Visual C++ Express 2008 to compile
 you will then need the stdint.h header.

Make sure you have correctly installed the required tools and that
they appear in your PATH environment variable.

The following process works for all platforms :
    1 - git clone /git::/.. "Analyz-X.XX.tar.gz"
    2 - tar zxvf Analyz-X.XX.tar.gz
    3 - cd Analyz-X.XX

=>To compile and install the Mamba library :
    1 - cd src
    2 - type :
    
        python setup.py build_ext build             (Linux)
        OR
        python setup.py build_ext build             (Windows with visual C++)
        python setup.py build_ext -cmingw32 build   (Windows with mingw32)
        
    3 - You can then install it.
    
        python setup.py install
    

Authors, Copyright & License
----------------------------

Copyright 2013, Pegot-Ogier Thomas <thomas.pegot@gmail.com>

Analyz is ruled by the **# License Terms**:

