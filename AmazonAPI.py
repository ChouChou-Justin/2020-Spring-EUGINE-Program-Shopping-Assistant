from amazon.api import AmazonAPI

AMAZON_ACCESS_KEY = 'AKIAJLGEZPE626PJDUDQ'
AMAZON_SECRET_KEY = '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'
AMAZON_ASSOC_TAG = 'research023-20'
amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)

product = amazon.lookup(ItemId='B00EOE0WKQ')






