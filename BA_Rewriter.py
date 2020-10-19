import random, time
string = 'আমি অসময়, অবেলায়: কিভাবে  অধিবেশন ছেড়ে চলে যাই। আমি বেহুশ। অধিবেশন'

a = ['অকাল', 'অসময়', 'অবেলায়', 'অদিন', 'কুদিন', 'দুঃসময়']
b = ['অচেতন', 'অজ্ঞান', 'আসাড়', 'জ্ঞানশূন্য', 'জ্ঞানহীন', 'বেহুশ']
c = ['অধিবেশন', 'সভা', 'সমিতি', 'সমাবেশ', 'মিটিং']
extra = ['।', ',', ':', ';']
word_lists = [a, b, c]

def converter(word, list):
	global string
	if word in list:
		string = string.replace(word, random.choice(list))

def main(str):
	for x in str.split('।'):
		for y in x.strip().split():
			for z in extra:
				y = y.replace(z, '')
			for w in word_lists:
				converter(y, w)

while True:
	main(string)
	print(string)
	time.sleep(2)
