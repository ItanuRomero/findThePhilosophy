# findThePhilosophy
App Flask that will run into wikipedia pages until find Philosophy

## This is a API to prove that is possible to find Philosophy page on wikipedia if you travel clicking on the first link of any wikipedia page
### Usage:
- Access the webpage and add /howManyTimes on the URL with GET method
- Then, add an ```?```, create a prop with the name of ```article``` and make the prop receive ```=``` your first page ```wikiArticle```
### Example:
```app.url/howManyTimes?article=abstraction```
### Returns
JSON with the keys - values:
- first: <String> First page - The one you put on ```article``` prop
- how_many_pages: <Int> Show how many pages the code run untill find the Philosophy wiki page
- pages: <List> Show every URL of the pages on the path to Philosophy

### Use case:
Request:

```/howManyTimes?article=abstraction```

Response:

```
{
  "first": "https://en.wikipedia.org/wiki/Abstraction",
  "how_many_pages": 4,
  "pages": [
    "https://en.wikipedia.org/wiki/Rule_of_inference",
    "https://en.wikipedia.org/wiki/Philosophy_of_logic",
    "Philosophy!!"
  ]
}
```

## Improvements are welcome, this is an open-source project - contribute!
