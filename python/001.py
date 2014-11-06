class tester:
    def __init__(self,start):
        self.state=start
    def nested(self,label):
        print(label,self.state)
        self.state+=1
