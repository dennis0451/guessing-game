class GuessingGame():
    def __init__(self, answer):
        self.answer = answer
    
    def guess(self, attempt = None, solved = False):
        self.attempt = attempt
        self.solved = solved
        if self.attempt == None:
            return solved
        elif self.attempt == self.answer:
            self.solved = True
            return "correct"
        elif self.attempt > self.answer:
            return "high"
        elif self.attempt < self.answer:
            return "low"


number_guess = GuessingGame(15) 
print(number_guess.answer)
print(number_guess.guess(5))
print(number_guess.guess(50))
print(number_guess.guess())
print(number_guess.solved)
print(number_guess.guess(15),number_guess.solved)