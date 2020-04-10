hello = "hello"
def world():
	return "world"

if __name__ == "__main__":
	print("{0} directly executed".format(__name__))
else:
	print("{0} imported".format(__name__))


