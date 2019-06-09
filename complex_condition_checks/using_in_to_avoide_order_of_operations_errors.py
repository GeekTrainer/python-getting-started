level = 'Gold'
payment = 'Incomplete'
free_movie = False

if level in('Gold','Silver') \
	and payment == 'Complete':
	free_movie = True

# Later in your code we can check if they earned the free movie
if free_movie:
	print('enjoy your movie')
else:
    print('Sorry you do not qualify')