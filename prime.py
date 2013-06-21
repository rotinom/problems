#!/usr/bin/env python

## \file Prime.py
##
## \author David Weber
##
## \brief This file will calculate all of the prime numbers from
##        1-N. Depending on the command line arguments, it will 
##        use one of several algorithms
##
## \Note Comments are in the doxygen style. Any recent
##       version of doxygen should be able to create appropriate
##       external documentation for this file

from optparse import OptionParser
import sys
from math import sqrt


## \brief This class provides several algorithms to calculate
##        prime numbers
class Prime:

    ## \param self Pointer to object instance
    ## \param N The upper bound used to locate prime numbers
    ## \returns True if N is valid, False otherwise
    def _validate(self, N):

        # Make sure that N is not "None" or
        # Negative or
        # equal to 0 or
        # equal to 1
        if None == N   or \
           N != abs(N) or \
           0 == N      or \
           1 == N:
            return False

        return True
    #end _validate

    ## \brief Method used to find the primes in a brute force
    ##        and very slow method
    ##
    ## \param self Pointer to object instance
    ##
    ## \param N The upper bound used to locate prime numbers
    ##        method.  
    ##
    ## \exception Exception An "Exception" will be raised if N
    ##            contains invalid data
    ##
    ## \returns List of the found prime numbers
    def bruteForce(self, N):

        # Validate the input
        if not self._validate(N):
             raise Exception("%s is an invalid upper bound." % N)

        # Declare the return value
        retValue = []
    
        # Loop through our possible values
        for i in xrange(2, N+1):
            notPrime = False
            
            # Calculate the square root, because this will be the upper
            # bounds of our inner loop
            squareRoot = sqrt(i)

            j = 2
            while (j <= squareRoot):

                # If evenly divisible, it's not prime, so exit the inner loop
                if i % j == 0:
                    notPrime = True
                    break

                j += 1 # Increment the inner loop

            # end while

            # Add it to the list if it is prime
            if not notPrime:
                retValue.append(i)             
        
            i += 1 # Increment the outer loop

        # end while

        # Return the list
        return retValue

    #end bruteForce


    ## \brief Method used to find the primes in a "better" brute force method
    ##
    ## \param self Pointer to object instance
    ##
    ## \param N The upper bound used to locate prime numbers
    ##        method.  
    ##
    ## \note This is better than the bruteForce() above, because we only check
    ##       to see if we are divisible by any found primes inside the inner
    ##       loop
    ##
    ## \exception Exception An "Exception" will be raised if N
    ##            contains invalid data
    ##
    ## \returns List of the found prime numbers
    def betterBruteForce(self, N):

        # Validate the input
        if not self._validate(N):
             raise Exception("%s is an invalid upper bound." % N)

        # Declare the return value
        retValue = []

        # Loop through our possible values
        for i in xrange(2, N+1):
            notPrime = False

            # Calculate the square root, because this will be the upper
            # bounds of our inner loop
            squareRoot = sqrt(i)

            # Loop through all of the found primes only
            for j in retValue:

                # No need to check primes larger than the square root of i                
                if j > squareRoot:
                    break

                # If evenly divisible, it's not prime, so bail out of
                # the inner loop
                if i % j == 0:
                    notPrime = True
                    break

            # end for

            # Add it to the list if it is prime
            if not notPrime:
                retValue.append(i)

            i += 1 # Increment the outer loop
        # end while

        # Return the list
        return retValue

    # end betterBruteForce



    def sieve_of_eratosthenes(self, N):

        # Validate the input
        if not self._validate(N):
             raise Exception("%s is an invalid upper bound." % N)

        # Declare the return value
        retValue = []

        max_value = int(sqrt(N))

        # Declare our data table
        data = [True] * (N+1)
        data[0] = False
        data[1] = False

        # Loop through data
        index = 2
        while index <= max_value:

            # Mark the intervals of index as not prime
            for i in xrange(index+index, N+1, index):
                # print "Marking %i" % i
                data[i] = False

            # Find the next possible prime
            index += 1
            while index < max_value and not data[index]: 
                index += 1

            # print "Next possible prime: %i" % index

        # Create our output
        for i in xrange(0, N+1):
            if data[i]:
                retValue.append(i)

        # Return the list
        return retValue

    # end sieve_of_eratosthenes




## \brief Method used to parse the command line arguments, and ensure
##        that the required elements have been filled out
##
## \returns "options" object returned from a call to the Python 
##          OptionParser object instance parse_args() call
def parseArgs():

    # Declare the option parser
    optParse = OptionParser()

    # Add options for the various algorithms
    optParse.add_option("-n", dest="N", action="store",
                      help="The upper limit of the primes you wish to find")

    # Add options for the various algorithms
    optParse.add_option("-b", dest="bruteForce", action="store_true",
                      help="Calculate primes using the brute force algorithm")

    optParse.add_option("-B", dest="betterBF", action="store_true",
                      help="Calculate primes using a better brute force algorithm")

    optParse.add_option("-s", dest="sieve", action="store_true",
                      help="Calculate primes using the Sieve of Eratosthenes")
    
    # If the user requested help, simply exit the application
    if "-h" in sys.argv:
        optParse.print_help()
        exit(0)

    # Verify that at least one algorithm has been specified
    algArgList = ["-b", "-B", "-s"]
    hasAlg = False

    # Look for one algorithm argument in the command line arguments
    for alg in algArgList:
        if alg in sys.argv:
            hasAlg = True

    # If no algorithms have been specified, exit
    if not hasAlg:
        print("*** No algorithm arguments specified ***")
        optParse.print_help()
        sys.exit(-1) 

    # Ensure that N has been passed in from the command line
    elif "-n" not in sys.argv:
        print("*** Upper bound not specified ***")
        optParse.print_help()
        sys.exit(-1) 

    # Parse the options
    (options, args) = optParse.parse_args()

    # Did they specify "-n" with nothing following it?
    # Does N have non-number items in it?
    # Is N passed in as a floating point number?
    if None == options.N   or \
       not options.N.isdigit() or \
       "." in options.N:
        print("*** -n must be followed by a positive integer ***")
        optParse.print_help()
        sys.exit(-1)      

    return options
#end parseArgs



## \brief "Main" function where the execution starts when called
##        as a stand-alone script
def Main():
    # Parse the command line arguments
    options = parseArgs()

    # Instantiate a prime class
    primeInstance = Prime()

    # Cast options.N to an integer (since we parse it as a string)
    N = int(options.N)

    # Calculate primes using the brute force method
    if options.bruteForce:

        # Try to calculate the primes in the given range
        try:
            primes = primeInstance.bruteForce(N)

        # Print out the exception
        except Exception, e:
            print e
            exit(-1)

        # Print out the primes
        print("The primes between 1 and %s using the brute force method are:" % options.N)
        for num in primes:
            print num


    # Calculate the primes using the "better" brute force method
    elif options.betterBF:

        # Try to calculate the primes in the given range
        try:
            primes = primeInstance.betterBruteForce(N)

        # Print out the exception
        except Exception, e:
            print e
            exit(-1)

        # Print out the primes
        print("The primes between 1 and %s using the \"better\" brute force method are:" % options.N)
        for num in primes:
            print num


    elif options.sieve:

        # Try to calculate the primes in the given range
        primes = primeInstance.sieve_of_eratosthenes(N)

        # Print out the primes
        print("The primes between 1 and %s using the Sieve of Eratosthenes method are:" % options.N)
        for num in primes:
            print num

#end Main



# This condition is true only if called as a stand alone script
# We call our main function to perform the majority of the work
if __name__ == "__main__":
    Main()
    

