import pickle

import matplotlib.pyplot as plt


def load_pkl(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)


def main():
    videos = load_pkl("vid_master")
    topic_definitions = load_pkl("topic_definitions")
    existing_topics_views = {}
    existing_topics_video_count = {}
    topic_average_views = {}

    for vid in videos:

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
        print("Title: " + vid.get("title"))
        print("Topics: " + str(topics_no_dupes))
        # print("Tags: " + str(vid.get("tags")))
        print("Views: " + str(vid.get("views")))
        # print("")

        # calculate total views for respective topics
        # create database of existing topics with respective views
        # and existing topics with video count
        for topic in topics_no_dupes:
            if vid.get("views") is not None:
                existing_topics_views[topic] = existing_topics_views.get(topic, 0) + int(vid.get("views"))
                existing_topics_video_count[topic] = existing_topics_video_count.get(topic, 0) + 1

    for (k, v) in existing_topics_views.items():
        print("KEY : " + k + " VALUE : " + str(v))
    for (k, v) in existing_topics_video_count.items():
        print("KEY : " + k + " VALUE : " + str(v))

    for (topic_views, views) in existing_topics_views.items():
        for (topic_count, count) in existing_topics_video_count.items():
            if topic_views == topic_count:
                topic_average_views[topic_views] = topic_average_views.get(topic_views, 0) + (views / count)

    for (k, v) in topic_average_views.items():
        print("Topic: " + k + " Average Views: " + str(v))

    # visualisation
    plt.bar(range(len(topic_average_views)), list(topic_average_views.values()), align="center")
    plt.xticks(range(len(topic_average_views)), list(topic_average_views.keys()))
    plt.xticks(rotation=90)
    plt.show()


if __name__ == "__main__":
    main()
