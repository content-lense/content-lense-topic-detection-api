from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7", framework="pt")
        
def processArticle(data):
    print("Process Article")

    body = data["body"]
    customTopics = data["customTopics"]
    totalTopics = data["totalTopics"]

    res = {
        "topics": []
    }

    try:
        labels = classifier(body, customTopics)["labels"]
        res["topics"] = labels[:int(totalTopics)]
        print("Finished")

    except Exception as e:
        print("error", e)

    print("res: ", res)
    return res
