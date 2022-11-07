from lib.py_quillbot import PyQuillbot

sentences_to_paraphrase = [
    'I am a student',
    'Having seen the impact of the revolution, I could not stop but wonder about its causes.',
    'your time is up',
    'Tell me everything you know about the language JavaScript.'
]

quill = PyQuillbot(multi_choices=True)
print('PyQuillbot initiated...')
print(f'Paraphrasing {len(sentences_to_paraphrase)} sentences...')
paraphrased_results = quill.paraphrase(sentences_to_paraphrase)
print('Paraphrasing complete:')
print(paraphrased_results)
