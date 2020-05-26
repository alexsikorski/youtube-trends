import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import json

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


def main():
    page_count = 0
    file_name = "data-"

    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    first_request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        chart="mostPopular",
        maxResults=10000,
        regionCode="US"
    )
    first_response = first_request.execute()

    # Dump first response
    with open("data/" + file_name + str(page_count) + ".json", "w") as outfile:
        json.dump(first_response, outfile)

    # Get all responses
    while page_count < 199:
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            chart="mostPopular",
            maxResults=10000,
            pageToken=obtain_page("data/" + file_name + str(page_count) + ".json"),
            regionCode="US"
        )
        response = request.execute()
        print("\rWriting page " + str(page_count) + "/199...", end="")
        page_count = page_count + 1

        with open("data/" + file_name + str(page_count) + ".json", "w") as outfile:
            json.dump(response, outfile)

        if page_count == 199:
            print("\rWriting page " + str(page_count) + "/199... All done!", end="")


def obtain_page(data_file):
    f = open(data_file)
    data = json.load(f)
    for (k, v) in data.items():
        if k == "nextPageToken":
            return v

    # path, dirs, files = next(os.walk("data"))
    # file_count = len(files)


if __name__ == "__main__":
    main()
