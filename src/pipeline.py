import textstat
import spacy
import textdescriptives as td
# todo: add english support: if language == "de" else "en_core_web_trf"
nlp = spacy.load("de_dep_news_trf")
nlp.add_pipe("textdescriptives")

# str = "de" | "en"
def calc_statistics(txt: str, language: str = "en"):
    textstat.set_lang(language)
    wienerSachtextIndex = textstat.wiener_sachtextformel(txt, 1)
    totalSyllables = textstat.syllable_count(txt)
    totalWords = textstat.lexicon_count(txt, removepunct=True)
    readingTimeInMin = totalWords/200
    totalSentences = textstat.sentence_count(txt)
    totalChars = textstat.char_count(txt, ignore_spaces=True)
    totalLetters = textstat.letter_count(txt, ignore_spaces=True)
    totalWordsLongerThanThreeSyllables = textstat.polysyllabcount(txt)
    totalSingleSyllableWords = textstat.monosyllabcount(txt)
    
    doc = nlp(txt)
    stats_dict_counts = doc._.counts
    totalUniqueWords = stats_dict_counts["n_unique_tokens"]
    stats_dict_sentence_length = doc._.sentence_length
    meanWordsPerSentence = stats_dict_sentence_length["sentence_length_mean"]
    medianWordsPerSentence = stats_dict_sentence_length["sentence_length_median"]
    stats_dict_token_length = doc._.token_length
    meanCharsPerWord = stats_dict_token_length["token_length_mean"]
    medianCharsPerWord = stats_dict_token_length["token_length_median"]

    res_dict = {
        "scores": {
            "wienerSachtextIndex": wienerSachtextIndex,
            "readingTimeInMinutes": readingTimeInMin
        },
        "descriptives": {
            "totalSyllables": totalSyllables,
            "totalChars": totalChars,
            "totalLetters": totalLetters,
            "totalWords": totalWords,
            "totalSentences": totalSentences,
            "meanWordsPerSentence": meanWordsPerSentence,
            "meanCharsPerWord": meanCharsPerWord,
            "medianWordsPerSentence": medianWordsPerSentence,
            "medianCharsPerWord": medianCharsPerWord,
            "totalWordsLongerThanThreeSyllables": totalWordsLongerThanThreeSyllables,
            "totalSingleSyllableWords": totalSingleSyllableWords,
            "totalUniqueWords": totalUniqueWords
        }
    }
    return res_dict


def processArticle(article):
    print("Process Article")
    res = {
        "heading": {},
        "summary": {},
        "body": {}
    }

    try:
        for part in article:
            if ((part in ["heading", "summary", "body"]) and (type(article[part]) == str )):
                print("calculate %s" % (part))
                part_json = calc_statistics(article[part])
                res[part] = part_json
        print("Finished: ", res)

    except Exception as e:
        print("error", e)

    return res
