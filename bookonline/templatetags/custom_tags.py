from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import SafeData, mark_safe
import re
import markdown as md

register = template.Library()



# NOTE IMPORTANT: when exporting from indesign setting should be to place the footnotes at end of the section not at end of peragraph


@register.filter()
@stringfilter
def mdparser(value):
  
    valuefirst = value.replace("\\n\\n", '\n\n')  
    
    # print(valuefirst)
    valuefirst = valuefirst.replace("\* \* \*", "---")

    # to seach first part of the footnote text ex, "[<sup><u>\[" from textline [<sup><u>\[3\]</u></sup>](\l)
    regex1 = r"\[<.*?\["
    # to seach 2nd part of the footnote text ex, "\]</u></sup>](\l)" from textline [<sup><u>\[3\]</u></sup>](\l)
    regex2 = r"\\].*?\)"
    # regex3 = r"\[\^\d\]"

    no_of_footnotes = re.findall(regex1, valuefirst)
    print(len(no_of_footnotes))
    half = int(len(no_of_footnotes)/2)
    print(half)
    replaced_1st_part = re.sub(regex1, "[^", valuefirst)
    replaced_2nd_part = re.sub(regex2,"]", replaced_1st_part, half) #replace 2nd regex but only to ist half footnotes
    finaltext = re.sub(regex2,"]: ", replaced_2nd_part)
    
    secondvalue = md.markdown( finaltext, extensions=['footnotes'] )


    x = secondvalue.count("<p>")
    counter = x-(x-1)
    for x in range(x):

        secondvalue = secondvalue.replace("<p>", '<p id="p' + str(counter)+ '">', 1)
        counter=+x+2
    #print(thirdvalue)    
  
    return mark_safe(secondvalue)


register.filter("mdparser", mdparser)












# @register.filter
# def low(value):
#     return value.lower()


# @register.filter
# @stringfilter
# def loww(value):

#     num1 = value.count("\n\n")
#     print(num1)


#     string = value.replace("\n\n", '</p><p id="p**">')
#     print(string)

#     char_remov = []

#     for x in range(num1):
#         char_remov.append("**")

#     string = value.replace("\n\n", '</p><p id="p**">')

#     coutr = num1+1
#     for char in char_remov:
#         nt = num1-(coutr-3)
#         n = str(nt)
#         string = string.replace(char, n, 1)
#         coutr = coutr-1

#     return string



# @register.filter()
# @stringfilter
# def mdparser(value):
#     valuefirst = value.replace("\\n\\n", "\n\n")
#     secondvalue = valuefirst.replace('\\"', '"')
#     thirdvalue = md.markdown( secondvalue, extensions=['footnotes'] )
#     x = thirdvalue.count("<p>")
#     counter = x-(x-1)
#     for x in range(x):

#         thirdvalue = thirdvalue.replace("<p>", '<p id="p' + str(counter)+ '">', 1)
#         counter=+x+2
#     #print(thirdvalue)
#     return mark_safe(thirdvalue)


# register.filter("mdparser", mdparser)





























# register.filter("markdown", markdown)
# register.filter("loww", loww)
