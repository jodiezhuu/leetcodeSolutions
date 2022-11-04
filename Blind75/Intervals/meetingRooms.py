def canAttendMeetings(intervals) -> bool:
	# create two arrays that store all start and end values 
	startArr = []
	endArr = []
	for start, end in intervals:
		startArr.append(start)
		endArr.append(end)
	# sort the two arrays
    startArr.sort()
    endArr.sort()
	# if the end time is greater than the next start time at the index then return false
	for i in range(len(startArr) - 1):
		if endArr[i] > startArr[i + 1]:
			return False
	return True