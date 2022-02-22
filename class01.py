class Stusent :
	def __init__(self, name, score) :
		self.name = name
		self.score = score
		print("我誕生了")
		

	def do_hw(self, hw) :
		print("我在做作業 !", hw)

	def study(self) :
		print("我在讀書")
		self.score += 5

	def sleep(self) :
		print("I am sleeping !")


s1 = Stusent("John", 100)
s2 = Stusent("Allen", 95)
students = [s1, s2]

for s in students :
	print(s.name, "的分數是", s.score)
	





