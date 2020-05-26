import json

videos = []


def main():
    file_name = "data/data-"
    file_count = 1

    while file_count < 200:
        f = open(file_name + str(file_count) + ".json")
        file_data = json.load(f)
        print("\rOpening file " + str(file_count) + "/200...", end="")
        file_count = file_count + 1

        items = file_data.get("items")
        for item in items:
            video = {"title": None, "views": None, "tags": None}
            snippets = item.get("snippet")
            statistics = item.get("statistics")

            for key, value in snippets.items():
                if key == "title":
                    video["title"] = value
                elif key == "tags":
                    video["tags"] = value

            for key, value in statistics.items():
                if key == "viewCount":
                    video["views"] = value
            videos.append(video)

    print("\rOpening file " + str(file_count) + "/200... All done!", end="")
    print()
    print(videos)


if __name__ == "__main__":
    main()