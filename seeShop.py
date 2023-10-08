from serpapi import GoogleSearch
import operator


print("Please enter a valid imgurl url for the image only(view the image on browser): ")
urlInput = input()

params = {
  "engine": "google_lens",
  "url": urlInput,
  "api_key": "api key"
}

search = GoogleSearch(params)
results = search.get_dict()       
shopping_results = results["visual_matches"]
results_num = len(shopping_results)
i = 0
resultsList = []

while i < results_num:
  if "price" in shopping_results[i]:
      if "$" in shopping_results[i]["price"]['currency']:
        price = shopping_results[i]["price"]['extracted_value']
        listing = {
          "name": shopping_results[i]["title"],
          "price": price,
          "source": shopping_results[i]["source"],
          "link": shopping_results[i]["link"]
        }
        resultsList.append(listing)
      else:
        i+=1
        continue
  i += 1
sorted_List = sorted(resultsList, key=operator.itemgetter('price'))

print("Currently the list of results is sorted by price. Would you like to group the websites before exporting results?(1 if yes/2 if no)")
x = input()
d=0
if x == '1':
  sorted_List = sorted(resultsList, key=operator.itemgetter('source'))
  with open('items.txt','w') as outFile:
    while d < len(sorted_List):
       line = sorted_List[d]['name'] + "\n" + "$" + str(sorted_List[d]['price']) + "\n" + sorted_List[d]['source'] + "\n" + sorted_List[d]['link'] + "\n" + "\n"
       outFile.write(line)
       d += 1
elif x == '2':
  with open('items.txt','w') as outFile:
    while d < len(sorted_List):
       line = sorted_List[d]['name'] + "\n" + "$" + str(sorted_List[d]['price']) + "\n" + sorted_List[d]['source'] + "\n" + sorted_List[d]['link'] + "\n" + "\n"
       outFile.write(line)
       d += 1
else:
   print("Invalid option")

