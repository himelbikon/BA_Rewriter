import random
sentences = 'আমি অসময়, অবেলায়: কিভাবে  অধিবেশন ছেড়ে চলে যাই। আমি বেহুশ। অধিবেশন'

def converter(string):
	a = ['অকাল', 'অসময়', 'অবেলায়', 'অদিন', 'কুদিন', 'দুঃসময়']
	b = ['অচেতন', 'অজ্ঞান', 'আসাড়', 'জ্ঞানশূন্য', 'জ্ঞানহীন', 'বেহুশ']
	c = ['অধিবেশন', 'সভা', 'সমিতি', 'সমাবেশ', 'মিটিং']
	extra = ['।', ',', ':', ';']
	lists = [a, b, c]

	for x in string.split('।'):
		for y in x.strip().split():
			for z in extra:
				y = y.replace(z, '')
			for list in lists:
				if y in list:
					string = string.replace(y, random.choice(list))
	return string


sentences = converter(sentences)
print(sentences)