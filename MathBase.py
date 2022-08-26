import math

class MathBase:
    @staticmethod
    def Hermit(argN, argX):             #Hermite polynomials
        factN = math.factorial(argN)
        answerHermit = 0
        powUnum = 1
        for it in range(int(argN/2) + 1):
            if(it % 2 == 0):
                powUnum = 1
            else:
                powUnum = -1
            answerHermit = answerHermit + powUnum * factN * ((2 * argX)**(argN - 2 * it)) / (math.factorial(it) * math.factorial(argN - 2 * it))

        return answerHermit

    @staticmethod
    def dnorm(argX, argMiu, argSg):     #Normal distribution
        partOneDnorm = 1 /(argSg * math.sqrt(2 * math.pi))
        partTwoDnorm = (-1 * ((argX - argMiu)**2) / (2 * argSg))
        return partOneDnorm * math.exp(partTwoDnorm)
