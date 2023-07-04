from elasticsearch_dsl import analyzer, token_filter


settings = {
    "number_of_shards": 5,
    "number_of_replicas": 1
}

custom_stop = token_filter(
    name_or_instance="custom_stop",
    type="stop",
    stopwords_path="analysis/stopwords.txt"
)

search_analyzer = analyzer(
    name_or_instance="search_analyzer",
    tokenizer="uax_url_email",
    filter=[
        "lowercase",
        "russian_morphology",
        "english_morphology",
        custom_stop
    ]
)