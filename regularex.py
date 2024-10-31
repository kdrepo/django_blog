import re

txt = '''is far greater than any other world. It is
this that the Gita terms
‘*parāprakritirjīvabhūtā*’[<sup><u>\[1\]</u></sup>](\l) which means that
the Consciousness-Force of the Supreme herself becomes the 
countries have forgotten this, but in India[<sup><u>\[2\]</u></sup>](\l)herefore, to think 
And to justify this by saying that outer circumstances and
times are not favourable, people are like this or that – is all a
falsehood. When in truth[<sup><u>\[3\]</u></sup>](\l) there exists no separate being other than one’s
own true self then, to use external circumstances, things and people as
an excuse for one’s inaction is a deluded way of seeing things and
negates the fundamental[<sup><u>\[4\]</u></sup>](\l) truth of one’s being, for so says the Vedanta,
‘ekamevadvitiyam’, meaning that there exist no two separate beings. In a
true sense, whatever we see around in the outside world, or which-soever
states of being or worlds we m [<sup><u>\[1\]</u></sup>](\l)fottnote content1[<sup><u>\[2\]</u></sup>](\l)fottnote content2
[<sup><u>\[3\]</u></sup>](\l)fottnote content3
[<sup><u>\[4\]</u></sup>](\l)fottnote content4

'''
# to seach first part of the footnote text ex, "[<sup><u>\[" from textline [<sup><u>\[3\]</u></sup>](\l)
regex1 = r"\[<.*?\["
# to seach 2nd part of the footnote text ex, "\]</u></sup>](\l)" from textline [<sup><u>\[3\]</u></sup>](\l)
regex2 = r"\\].*?\)"
# regex3 = r"\[\^\d\]"

no_of_footnotes = re.findall(regex1, txt)
half = int(len(no_of_footnotes)/2)

replace_1st_part = re.sub(regex1, "[^", txt)
replace_2nd_part = re.sub(regex2,"]", replace_1st_part, half) #replace 2nd regex but only to ist half footnotes

replace_last_remaining = re.sub(regex2,"]: ", replace_2nd_part)

print(replace_last_remaining)











