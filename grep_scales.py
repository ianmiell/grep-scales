from shutit_module import ShutItModule

class grep_scales(ShutItModule):

	def build(self, shutit):
		afile = r'''THIS LINE IS THE 1ST UPPER CASE LINE IN THIS FILE.
this line is the 1st lower case line in this file.
This Line Has All Its First Character Of The Word With Upper Case.

Two lines above this line is empty.
And this is the last line.
'''
		shutit.send_file('afile',afile)
		shutit.send('alias grep=grep')
		afile_message = '''I have created a file called 'afile' that looks like this: 
BEGINS
''' + afile + '''
ENDS
'''
		follow_on_context={'check_command':'ls','context':'docker'}
		#shutit.challenge('move file afile to filename: 1',challenge_type='golf',expect='1',follow_on_context=follow_on_context)
		shutit.challenge(afile_message + '''
For your first task, grep out the last line, ie the one that reads: 'And this is the last line.'.''','And this is the last line.',hints=['last','grep last afile'])
		shutit.golf(afile_message + 'Return a count of the number of lines with "UPPER" in it (case sensitive)','1',hints=['-c','ask again to get answer','grep -c UPPER afile'])
		shutit.golf(afile_message + 'Return a count of the number of lines with "UPPER" in it (case insensitive)','2',hints=['-c','-i','ask again to get answer','grep -c -i UPPER afile'])
		shutit.golf(afile_message + 'Return lines that have the word "in" in it (case insensitive)','264200b0557e7c2e75cffc57778311f4',expect_type='md5sum',hints=['-w','-i','ask again to get answer','grep -w -i in afile'])
		shutit.golf(afile_message + '''Return lines that DON'T have the word 'case' (case insensitive) in it.''','ca75d0d8558569109e342ac5e09c4d01',expect_type='md5sum',hints=['-v','-i','ask again to get answer','grep -v case afile'])
		shutit.golf(afile_message + '''Return line with "UPPER" in it, along with the line number.''','cc9246de53156c4259be5bf05dacadf6',expect_type='md5sum',hints=['-n','ask again to get answer','grep -n UPPER afile'])
		shutit.golf(afile_message + 'Print the line after the empty line.','63b6f5fd46648742a6f7aacff644dd92',expect_type='md5sum',hints=['-A','-A1','ask again to get answer','grep -A1 ^$ afile'])
		shutit.golf(afile_message + 'Print the two lines that come before the first line with nothing in it.','444cc6679be200fc6579678b6afe19e9',expect_type='md5sum',hints=['-B','-B2','^$ to match the empty line','ask again to get answer','grep -B2 ^$ afile'])
		shutit.golf(afile_message + 'Print the line before the empty line, the empty line, and the line after.','7ba4233c4599e0aefd11e93a66c4bf17',expect_type='md5sum',hints=['-C','-C1','ask again to get answer','grep -C1 ^$ afile'],congratulations='Well done, all done!')
		#-o, --only-matching Print only the matched (non-empty) parts of a matching line, with each such part on a separate output line.
		#-l, --files-with-matches Suppress normal output; instead print the name of each input file from which output would normally have been printed.  The scanning will stop on the first match.
		#-r
		#-e
		return True

def module():
	return grep_scales(
		'tk.shutit.grep_scales.grep_scales', 1845506479.0001,
		description='Practice your grep scales!',
		maintainer='ian.miell@gmail.com',
		delivery_methods=['docker'],
		depends=['shutit.tk.setup']
	)

