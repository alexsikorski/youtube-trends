import pickle


def load_pkl(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)


def main():
    videos = load_pkl("vid_master")
    topic_definitions = load_pkl("topic_definitions")

    for vid in videos:
        print("Title: " + vid.get("title"))

        topics = vid.get("topics")
        topics_no_dupes = []

        # defines topic definition
        if topics is not None:
            for i, topic in enumerate(topics):
                for (key, value) in topic_definitions.items():
                    if topic == key:
                        topics[i] = value

        # removes duplicates
        if topics is not None:
            topics_no_dupes = list(dict.fromkeys(topics))

        print("Topics: " + str(topics_no_dupes))
        print("Tags: " + str(vid.get("tags")))
        print("Views: " + str(vid.get("views")))
        print("")


if __name__ == "__main__":
    main()
