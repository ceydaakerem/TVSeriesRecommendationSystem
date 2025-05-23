from veriler import movieandseries  # Verileri dış dosyadan al
def get_recommendations(year, rating, content_type, language):
    key = (year, rating, content_type, language)
    if key in movieandseries:
        print("\nRecommended for you:")
        for i, title in enumerate(movieandseries[key], 1):
            print(f"{i}. {title}")
    else:
        print("\nSorry, no exact matches found.")
        
        similar = [v for k,v in movieandseries.items() if k[2] == content_type and k[3] == language]
        if similar:
            print("\nHere are some similar recommendations:")
            for i, titles in enumerate(similar[0], 1):
                print(f"{i}. {titles}")
        else:
            print("No similar content available.")

print("Welcome to the Recommendation System!")

try:
    year = int(input("Enter the release year (e.g. 2020): "))
    rating = int(input("Enter the rating (1-5): "))
    content_type = input("Movie or Series? ").strip().lower()
    language = input("Language (english/turkish): ").strip().lower()

    if content_type not in ["movie", "series"]:
        print("Please enter either 'movie' or 'series'.")
    elif language not in ["english", "turkish"]:
        print("Please enter either 'english' or 'turkish'.")
    elif rating < 1 or rating > 5:
        print("Rating must be between 1 and 5.")
    else:
        get_recommendations(year, rating, content_type, language)

except ValueError:
    print("Invalid input! Please enter numbers for year and rating.")
       
       
       
       
       
       
       
       