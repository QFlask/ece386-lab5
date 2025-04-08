# Art Institute of Chicago API

Prompt engineering to have a LLM make a Python script to query exhibitions.

***Student**, Complete below.*

## Stats

### How many different prompts did you have to try before it worked?

I only needed to use one prompt.

### How well did the final produced script work?

The final script worked very well and even included a nice UI to split each exhibition. It listed an exhibition and all artworks within that exhibition. 

If I used multiple key terms, it returned all exhibitions that contained any of the search terms.

### What are some of the artwork titles from the exhibition "Ink on Paper: Japanese Monochromatic Prints (2009)"

Here are the artwork titles from that exhibition exactly displayed from the ClaudeAI script:

4. Exhibition: Ink on Paper: Japanese Monochromatic Prints (2016)
   Date: N/A to N/A
   Artworks:
   1. The Poetess Ukon, from the series The Thirty-six Immortal Women Poets (Nishikizuri onna sanjurokkasen)
   2. The Poetess Michitsuna no Haha, from the series "The Thirty-six Immortal Women Poets (Nishikizuri onna sanjurokkasen)"
   3. The Poetess Shunzei no Musume, from the series The Thirty-six Immortal Women Poets (Nishikizuri onna sanjurokkasen)
   4. The Poetess Gishumon-in no Tango, from the series The Thirty-six Immortal Women Poets (Nishikizuri onna sanjurokkasen)
   5. Sea Coast, Futomi
   6. Tanabata Dance
   7. Actor as a Standing Beauty
   8. The Demon Shutendoji, from the album Yamato Irotake
   9. The Tanabata Festival, from the series "Amusements of the Five Festival Days (Gosetsu asobi)"
   10. Summer Bush Clover (Natsuhagi), from the series Choicest Odes upon Flowers of the Four Seasons (Shuku awase, shiki no hana)
   11. Two Actors in a Drama
   12. Hara: A Line at the Foot of Mt. Fuji (Suso ichimonji), No. 14 from the series "Munakata's Tokaido (Tokaido Munakata hanga)"
   13. Miyahito of the Ogiya, Whose Assistants Are Tsubaki and Shirabe (Ogiya uchi Miyahito, Tsubaki, Shirabe)
   14. The Evening Bell at Miidera (Mii no banshō), from the series "Eight Views in Omi Province (Omi hakkei no uchi)"
   15. Lingering Snow at Asukayama (Asukayama no bosetsu), from the series "Eight Views in the Environs of Edo (Edo kinko hakkei no uchi)"
   16. Landscape with Waterfall
   17. The Monkey Bridge in Winter
   18. A Bat Flying near a Pine Tree
   19. Scene in the Yoshiwara, from the series "Views of Yoshiwara"
   20. Human Beings
   21. Ancient People
   22. Girl in Cotton Dress
   23. Structural Interior of Tengaimon Gate
   24. The Bright of Evening
   25. Bird and Fox
   26. The Night Visit, from the series "Story of the Cormorant"
   27. Descending Geese
   28. Badger, from the series "Mirror of Stone Rubbings of Views of the Provinces" (Kohon meihitsu ishizuri kagami)
   29. Tea Kettle, section of a sheet from the series "Mirror of Stone Rubbings of Views of the Provinces" (Kohon meihitsu ishizuri kagami)
   30. Seikenji Fuji, from the series "Mirror of Stone Rubbings of Views of the Provinces (Kohon meihitsu ishizuri kagami)"
   31. Proportion I
   32. Partial Rosette Segment from a Roof Tile and Peony from a Roof Tile
   33. Partial Rosette Segment from a Roof Tile and Peony from a Roof Tile
   34. Flower of the Evergreen Magnolia
   35. The Actors Nakamura Takesaburō as Kewaizaka no Shōshō and IchikawaDanjurō II as Soga Gorō

## Prompt

### Share the conversation URL

https://claude.site/artifacts/dc924d78-904b-4d3d-a3f9-f13a297b9294

## Paste your prompt here

I want you to complete some Python code for me. the ultimate goal of this script is to view art exhibitions from the Art Institute of Chicago using the Art Institute of Chicago API.
I want the Python script to do the following things:
- Accept a search term from the user
- Search the Art Institute of Chicago API for exhibitions marching this search term **and** that have artwork titles using a **GET** request
- Display the titles of the artwork for those exhibitions to the user
- Loop until the user exits

##Here is the background information for the API:
For example, you can access the /artworks listing endpoint in our API by visiting the following URL to see all the published artworks in our collection:

https://api.artic.edu/api/v1/artworks

If you want to search and filter the results, you can do so via our search endpoints. For example, here is a full-text search (opens new window)for all artworks whose metadata contains some mention of cats:

https://api.artic.edu/api/v1/artworks/search?q=cats

Here is the same search, but filtered to only show artworks that are in the public domain:

https://api.artic.edu/api/v1/artworks/search?q=cats&query[term][is_public_domain]=true

Our API accepts queries through both GET and POST. It might be easier to visualize how the GET query above is structured by comparing it to its POST equivallent:

curl --location --request POST 'https://api.artic.edu/api/v1/artworks/search' \
--header 'Content-Type: application/json' \
--data-raw '{
    "q": "cats",
    "query": {
        "term": {
            "is_public_domain": true
        }
    }
}'
For production use, we recommend using GET and passing the entire query as minified URL-encoded JSON via the params parameter. For example:

https://api.artic.edu/api/v1/artworks/search?params=%7B%22q

##Here is background information for getting exhibitions from the API

GET /exhibitions
A list of all exhibitions sorted by last updated date in descending order. For a description of all the fields included with this response, see here.

#Available parameters:
ids - A comma-separated list of resource ids to retrieve
limit - The number of resources to return per page
page - The page of resources to retrieve
fields - A comma-separated list of fields to return per resource
include - A comma-separated list of subresource to embed in the returned resources. Available options are:
artworks
sites
Example request: https://api.artic.edu/api/v1/exhibitions?limit=2

###Python template

use the `requests` library for making the GET requests

```Python
def search_exhibitions(term: str) -> list[int]:
    '''Make a request to exhibitions/search for the search term,
    using Elasticsearch `exists` option to only return results where the `artwork_titles` field is not empty
    Process the result and return a list of exhibitions IDs.
    '''
	
def display_exhibitions(list[int]) -> None:
	'''Given a list of exibition IDs, make a GET request to retrieve the exhibition titles and print them to the user	
	'''

def main():
	#TODO: create a continuous loop to:
	# - ask for a search term from the user
	# - Accept a search term from the user
	# - Search the Art Institute of Chicago API for exhibitions marching this search term  **and** that have artwork titles using a **GET** request
	# - Display the titles of the artwork for those exhibitions to the user

```