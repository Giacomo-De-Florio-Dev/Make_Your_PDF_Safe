# Config file of MyPDFs

# Check the Operating System

"""
WARNING: BY CHANGING THIS OPTION, THE PROGRAM PROBABLY NO LONGER WORKS CORRECTLY.

USAGE: 
        check_the_platform = ["< Y or N >", "< OS IDENTIFIER >"]
        
        >>> OPTIONS
                        check_the_platform[0]: Y = Yes, N = No

                        check_the_platform[1]: PLATFORM:OS:WIN = Windows
                                               PLATFORM:OS:LINUX = Linux and distros
                                               PLATFORM:OS:MACOS = Mac Os

        >>> DEFAULT :
                        check_the_platform = ["Y", "PLATFORM:OS:WIN"]


"""

check_the_platform = ["Y", "PLATFORM:OS:WIN"]