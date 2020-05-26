import pickle


def load_videos(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

def main():
    videos = load_videos("vid_master")
    print(videos)
    for vid in videos:
        print(vid.get("topics"))

if __name__ == "__main__":
    main()
