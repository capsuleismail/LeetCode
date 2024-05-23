class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        if n == 2:
            return 0

        primes = [True]*n
        primes[0], primes[1] = False, False
        for i in range(2, int(n//2)+1):
            if primes[i]:
                #square i, because if I have a factor that it was less than I it should mark as the previous iteration of the loop
                for x in range(i*i, n, i):
                    primes[x] = False
                    
        return len([i for i in range(n) if primes[i]])
                    
            
            
        