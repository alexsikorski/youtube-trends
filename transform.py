import json
import pickle

videos = []


def save_pkl(data, name):
    with open(name + ".pkl", "wb") as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)


def main():
    file_name = "data/data-"
    file_count = 1

    while True:
        try:
            f = open(file_name + str(file_count) + ".json", "r", encoding="utf8", errors="ignore")
        except FileNotFoundError:
            print("\rAll done!", end="")
            break
        file_data = json.load(f)
        print("\rOpening file data-" + str(file_count) + ".json...", end="")
        file_count = file_count + 1

        items = file_data.get("items")
        for item in items:
            video = {"title": None, "views": None, "tags": None, "topics": None}
            snippets = item.get("snippet")
            statistics = item.get("statistics")
            topics = item.get("topicDetails")

            for key, value in snippets.items():
                if key == "title":
                    video["title"] = value
                elif key == "tags":
                    video["tags"] = value

            for key, value in statistics.items():
                if key == "viewCount":
                    video["views"] = value

            if topics is not None:
                for key, value in topics.items():
                    if key == "relevantTopicIds":
                        video["topics"] = value

            videos.append(video)

    save_pkl(videos, "vid_master")


if __name__ == "__main__":
    main()
