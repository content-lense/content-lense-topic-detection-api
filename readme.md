# Welcome to Content Lense Topic Detection API 👋

<p align="center">
  <img src="https://user-images.githubusercontent.com/15559708/195378979-701254fa-ada7-41d4-abc7-494a40207a6d.png" />
</p>

_This is a microservice APIof Content Lense, a project that aims at enabling publishers to easily gain insights into their content._
_This API determines n topics of the given article from a given list of topics._

Please note that this repository is part of the [Content Lense Project](https://github.com/content-lense) and depends on the [Content Lense API](https://github.com/content-lense/content-lense-api).


## Running the service with Docker

Start the container with

`docker compose up`

Use `-d` to run it in the background.

## Using the api

### Analyse articles

To analyse an article send a post request to the `/articles` endpoint as `Content-Type: application/json` with the following stucture:

```json
{
  "body": "The entire article.",
  "customTopics": ["Wirtschaft", "Fußball", "Politik", "Wissenschaft", "Geld"],
  "totalTopics": 3
}
```

The return type looks like the following:

```json
{
    "topics": ["Wissenschaft", "Politik", "Geld"]
}
```

### Sources

- Huggingfaces `Zero-Shot-Classification` (https://huggingface.co/docs/transformers/v4.15.0/en/main_classes/pipelines#transformers.ZeroShotClassificationPipeline)
- Pretrained Model with German Dataset (https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli?candidateLabels=politics%2C+economy%2C+entertainment%2C+environment&multiClass=false&text=Angela+Merkel+ist+eine+Politikerin+in+Deutschland+und+Vorsitzende+der+CDU)

## Notes

- as Docker is not _yet_ configured to use the GPU, it takes around 3 minutes to determine a topic for one article (30 topics, 700 words) 
- we tested with GPU: this leads to less than a minute (obviously depending on the GPU instance)
  - e.g. ~ 20 sec for NVIDIA Tesla M60

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
