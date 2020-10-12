import urllib.request

req = urllib.request.Request('http://www.voidspace.org.uk')
with urllib.request.urlopen(req) as response:
   the_page = response.read()
   the_page2 = str(the_page).replace("PUBLIC", "SRUBLIC")


the_page3 = bytes(the_page2, 'utf-8')



print(type(the_page3))

