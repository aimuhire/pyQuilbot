import json

from playwright.sync_api import sync_playwright


class PyQuillbot:
    def __init__(self, autoflip='true', fthresh=9, strength=5, wikify='false', quoteIndex=1, multi_choices=False):
        self.autoflip = "true"
        self.fthresh = 9
        self.strength = 5
        self.wikify = "false"
        self.quoteIndex = quoteIndex if not multi_choices else 0

    def paraphrase(self, sentences):

        with sync_playwright() as p:
            paraphrased_data = {}
            browser = p.chromium.launch()
            page = browser.new_page(extra_http_headers={
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"})
            page.goto('https://quillbot.com')
            for i, sentence in enumerate(sentences):
                url = f"https://quillbot.com/api/paraphraser/single-paraphrase/2?text={sentence}&strength={self.strength}&autoflip={self.autoflip}&wikify={self.wikify}&fthresh={self.fthresh}&quoteIndex={self.quoteIndex}"
                page.goto(url)
                try:
                    jsonContent = json.loads(page.inner_text('pre'))
                    # the index stuff is a cleanup method that may cause issues sometimes :)
                    paraphrased_data[sentence] = [choice['alt'][choice['alt'].index("\"")+1:]
                                                  for choice in jsonContent['data'][0]['paras_3']]
                except Exception as e:
                    paraphrased_data[sentence] = [None]
                    print("Skipped sentence due to error ", e)
                print(f'progress: {i+1}/{len(sentences)}')
                page.goto('https://quillbot.com')

        return paraphrased_data
