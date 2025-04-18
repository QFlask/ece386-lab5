import requests
import json
import sys


def search_exhibitions(term: str) -> list[int]:
    """Make a request to exhibitions/search for the search term,
    using Elasticsearch `exists` option to only return results where the `artwork_titles` field is not empty
    Process the result and return a list of exhibitions IDs.
    """
    base_url = "https://api.artic.edu/api/v1/exhibitions/search"

    # Build the query with both search term and ensuring artwork_titles exists
    params = {
        "q": term,
        "query": {"exists": {"field": "artwork_titles"}},
        "limit": 10,  # Limiting to 10 results for clarity
    }

    # URL encode the params JSON
    encoded_params = json.dumps(params)

    # Make the GET request
    response = requests.get(f"{base_url}?params={encoded_params}")

    if response.status_code != 200:
        print(f"Error: API returned status code {response.status_code}")
        return []

    data = response.json()

    # Extract exhibition IDs from the response
    exhibition_ids = []
    if "data" in data:
        for exhibition in data["data"]:
            if "id" in exhibition:
                exhibition_ids.append(exhibition["id"])

    return exhibition_ids


def display_exhibitions(exhibition_ids: list[int]) -> None:
    """Given a list of exhibition IDs, make a GET request to retrieve the exhibition titles
    and artwork titles, then print them to the user
    """
    if not exhibition_ids:
        print("No exhibitions found matching your search criteria.")
        return

    # We'll use the include parameter to embed artwork information
    base_url = "https://api.artic.edu/api/v1/exhibitions"
    ids_str = ",".join(str(id) for id in exhibition_ids)

    # Make request with IDs and include artworks
    response = requests.get(f"{base_url}?ids={ids_str}&include=artworks")

    if response.status_code != 200:
        print(f"Error retrieving exhibition details: {response.status_code}")
        return

    data = response.json()

    # Display each exhibition with its artwork titles
    if "data" in data:
        for i, exhibition in enumerate(data["data"]):
            print(f"\n{i+1}. Exhibition: {exhibition.get('title', 'Untitled')}")
            print(
                f"   Date: {exhibition.get('start_date', 'N/A')} to {exhibition.get('end_date', 'N/A')}"
            )

            # Check if artwork_titles exists and is not empty
            artwork_titles = exhibition.get("artwork_titles", [])
            if artwork_titles:
                print("   Artworks:")
                for j, title in enumerate(artwork_titles):
                    print(f"   {j+1}. {title}")
            else:
                print("   No artwork titles available.")

            print("-" * 50)
    else:
        print("No exhibition details found.")


def main():
    print("Welcome to the Art Institute of Chicago Exhibition Search")
    print("Enter a search term to find exhibitions, or 'exit' to quit.")

    while True:
        # Ask for a search term
        search_term = input("\nEnter search term: ").strip()

        # Check if user wants to exit
        if search_term.lower() in ["exit", "quit"]:
            print(
                "Thank you for using the Art Institute of Chicago Exhibition Search. Goodbye!"
            )
            sys.exit(0)

        # Skip empty searches
        if not search_term:
            print("Please enter a valid search term.")
            continue

        # Search for exhibitions matching the term with artwork titles
        print(f"Searching for exhibitions related to '{search_term}'...")
        exhibition_ids = search_exhibitions(search_term)

        # Display the results
        display_exhibitions(exhibition_ids)


if __name__ == "__main__":
    main()
