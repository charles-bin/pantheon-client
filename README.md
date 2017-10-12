
# Pantheon  

### Using the API

URL  
---  

`/games/` or `/games/<id>/` or `/games/?<filter-field>=<filter-parameter>`

Methods  
-------  
GET | POST | PUT | DELETE  

Data Params  
-----------  
 {  
 	"title": [string],  
 	"image": [string],  
 	"description": [string],  
 	"developer": [string],  
 	"genre": [string],  
 	"published": [date],  
 	"rank": [integer]  
 }

Filter-Fields  
-------------  
filter-title  
filter-description  
filter-developer  
filter-genre  
filter-before  (filters games published before date)  
filter-after  (filters games published after date)  
filter-rank-lt  (filters games with rank lower than)  
filter-rank-gt  (filters games with rank greater than)  
