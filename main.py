class srand:
    def __init__(self, seed):
        self.state = seed

    def rand(self):
        self.state = (214013 * self.state + 2531011) & 0xFFFFFFFF
        return (self.state >> 16) & 0x7FFF

random = srand(7355608)
for i in range(10):
    print(random.rand())
