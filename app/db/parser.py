import json

from models import Subject

# Assuming this is the data string you provided (as a Python string, not a JSON file)
data_str = """{
    "id": 13,
    "type": 4,
    "name": "CLANNAD",
    "name_cn": "",
    "infobox": "{{Infobox Game...}}",
    "platform": 4001,
    "summary": "季節は春...",
    "nsfw": false,
    "tags": [
        {"name": "key", "count": 2232},
        {"name": "CLANNAD", "count": 1816},
        {"name": "麻枝准", "count": 1556},
        {"name": "Galgame", "count": 1475},
        {"name": "催泪弹", "count": 797},
        {"name": "家族", "count": 711},
        {"name": "人生", "count": 688},
        {"name": "亲情", "count": 653},
        {"name": "泣きゲー", "count": 465},
        {"name": "爱情", "count": 270},
        {"name": "PC", "count": 235}
    ],
    "score": 8.9,
    "score_details": {"1": 41, "2": 5, "3": 10, "4": 23, "5": 53, "6": 126, "7": 330, "8": 913, "9": 1653, "10": 2049},
    "rank": 12,
    "date": "2004-04-28",
    "favorite": {"wish": 2192, "done": 5993, "doing": 814, "on_hold": 681, "dropped": 156},
    "series": false
}"""

# Load the string into a Python dictionary
data = json.loads(data_str)


# Define a helper function to create the Game object
def parse_game_data(data: dict):
    # Parse tags into a list of tag names (as strings)
    tags = [tag["name"] for tag in data.get("tags", [])]

    # Parse score details into individual score categories
    score_details = data.get("score_details", {})
    score_details_values = [score_details.get(str(i), 0) for i in range(1, 11)]

    # Create the Game object
    game = Subject(
        id=data.get("id"),
        name=data.get("name"),
        name_cn=data.get("name_cn"),
        infobox=data.get("infobox"),
        platform=data.get("platform"),
        summary=data.get("summary"),
        nsfw=data.get("nsfw"),
        tags=tags,
        score=data.get("score"),
        score_details_1=score_details_values[0],
        score_details_2=score_details_values[1],
        score_details_3=score_details_values[2],
        score_details_4=score_details_values[3],
        score_details_5=score_details_values[4],
        score_details_6=score_details_values[5],
        score_details_7=score_details_values[6],
        score_details_8=score_details_values[7],
        score_details_9=score_details_values[8],
        score_details_10=score_details_values[9],
        rank=data.get("rank"),
        date=data.get("date"),
        favorite_wish=data["favorite"].get("wish", 0),
        favorite_done=data["favorite"].get("done", 0),
        favorite_doing=data["favorite"].get("doing", 0),
        favorite_on_hold=data["favorite"].get("on_hold", 0),
        favorite_dropped=data["favorite"].get("dropped", 0),
        series=data.get("series"),
    )

    return game


# Parse the game data and create the Game object
game_object = parse_game_data(data)

# Display the created Game object (you can further process this as needed)
print(game_object)
