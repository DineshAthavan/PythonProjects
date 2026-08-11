from bs4 import BeautifulSoup


with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents,"html.parser")

#print(soup.title)
#print(soup.title.name)
#print(soup.title.string)


#print(soup) #prints whole html file without indentation
#print(soup.prettify()) #prints whole html file with indentation

all_anchor_tags = soup.findAll(name="a")
print(all_anchor_tags)

#Extracting info from the anchor tags
for tag in all_anchor_tags:
    print(tag.get_text())
    print(tag.get("href"))

heading = soup.find(name='h1',id='name')#Searching for specific h1 using id.
# Use findAll for getting all h1 with the same id. find returns the very first h1.
print(heading)

section_heading = soup.find(name='h3',class_='heading')#class_ is used to avoid using keywords
print(section_heading)

#Identifying needed elements
company_url = soup.select_one(selector="p a")#Use select all to get all matching content
# satisfying selector in a list. This selector looks for anchor tag inside a paragraph tag.
print(company_url)
print(company_url.get("href"))

#Using selector with id instead of html tags.
name = soup.select_one(selector='#name')# # is used for mentioning id
print(name)

headings = soup.select(selector='.heading')# . is used for mentioning class. Returns a list.
print(headings)