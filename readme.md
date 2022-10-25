# Welcome to Content Lense Text Complexity API 👋

<p align="center">
  <img src="https://user-images.githubusercontent.com/15559708/195378979-701254fa-ada7-41d4-abc7-494a40207a6d.png" />
</p>

_This is a microservice APIof Content Lense, a project that aims at enabling publishers to easily gain insights into their content._
_This API calculates the complexity, reading time and more basic stats of the given article._

Please note that this repository is part of the [Content Lense Project](https://github.com/content-lense) and depends on the [Content Lense API](https://github.com/content-lense/content-lense-api).


## Building the Docker image

Build the Docker image by running:

`docker build -f Docker/Dockerfile -t content-lense-text-complexity:latest .`

## Running the service

Start the container with

`docker run -it --rm -p 5001:5001 content-lense-text-complexity`

## Using the api

### Analyse articles

To analyse an article send a post request to the `/articles` endpoint as `Content-Type: application/json` with the following stucture:

```json
{
    "heading":"The Headline of the Article",
    "summary":"A short summary / abstract of the article",
    "body": "The entire fulltext"
}
```
The return type looks like the following:

```javascript
{
    "body": {
        "descriptives": {
            "averageWordsPerSentence": 8.2,
            "meanCharsPerWord": 4.439024390243903,
            "meanWordsPerSentence": 6.833333333333333,
            "medianCharsPerWord": 4.0,
            "medianWordsPerSentence": 5.5,
            "totalChars": 190,
            "totalLetters": 182,
            "totalSentences": 5,
            "totalSyllables": 52,
            "totalUniqueWords": 37,
            "totalWords": 41,
            "totalWordsLongerThanThreeSyllables": 3,
            "totalSingleSyllableWords": 33
        },
        "scores": {
            "readingTimeInMinutes": 2.79,
            "wienerSachtextIndex": 1.2 // see https:/
        }
    },
    "heading": {/*... same result keys as for body ... */},
    "summary": {/*... same result keys as for body ... */}
}
```

### Sources

- `wienerSachtextIndex` (https://de.wikipedia.org/wiki/Lesbarkeitsindex)
- used Libraries
    - `TextStat` (https://github.com/textstat/textstat)
    - `TextDescriptives` (https://hlasse.github.io/TextDescriptives)
    - `Spacy Models` (https://spacy.io/usage/models)


## Supported by

Media Tech Lab [`media-tech-lab`](https://github.com/media-tech-lab)

<a href="https://www.media-lab.de/en/programs/media-tech-lab">
    <img src="https://raw.githubusercontent.com/media-tech-lab/.github/main/assets/mtl-powered-by.png" width="240" title="Media Tech Lab powered by logo">
</a>

---

Cloud Creators GmbH [`cloud-creators`](https://cloud-creators.de)


<a href="https://cloud-creators.de">
    <img src="https://cloud-creators.de/assets/images/cc-logo.svg" width="240" title="Supported by Cloud Creators GmbH">
</a>
