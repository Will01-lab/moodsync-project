def get_mood():
    mood = input("How are you feeling? ").lower().strip()
    return mood


def recommend_song(mood):
    songs = {
        "happy": ["Happy - Pharrell", "Good as Hell - Lizzo"],
        "sad": ["Someone Like You - Adele", "Stay - Rihanna"],
        "stressed": ["Weightless - Ambient", "Lo-fi Beats"],
        "tired": ["Chill Vibes", "Soft Piano"],
        "energetic": ["Stronger - Kanye West", "POWER - Kanye West"]
    }
    
    if mood in songs:
        print("Recommended songs:")
        for song in songs[mood]:
            print("-", song)
    else:
        print("No recommendations for that mood yet.")


def main():
    mood = get_mood()
    recommend_song(mood)


main()
