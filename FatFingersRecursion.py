dict_nums = {

'1' : ['1', '2', '4'],
'2' : ['1', '2', '3', '5'],
'3' : ['2', '3', '6'],
'4' : ['1', '4', '5', '7'],
'5' : ['2', '4', '5', '6', '8'],
'6' : ['3', '5', '6', '9'],
'7' : ['4', '7', '8', '*'],
'8' : ['5', '7', '8', '9', '0'],
'9' : ['6', '8', '9', '#'],
'0' : ['8', '*', '0', '#'],

}
out = []
def possibilities(number, accum='', retList=[]):
	#checking if this is last run
	last = (len(number) == 1)

	#for each digit in number, we are looping over possible presses
	for num in dict_nums[number[0]]:
		#setting current comination = received accumalated string from previous recursive calls + current digit
		curr = accum + num
		# print (curr, last)
		if last:
		#if this is last run we are appending the string to retList
			retList.append(curr)
			# print(retList)
		else:
		#else we are passign accumalted test to recurse over rest of the string
			possibilities(number[1:],curr, retList)
	return retList

print (possibilities("123"))

