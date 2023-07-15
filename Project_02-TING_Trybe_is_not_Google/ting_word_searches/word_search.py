def exists_word(word, instance, show_line_content=False):
    files_containing_word = []
    for txt_file in instance._data:
        found = []
        for index, line in enumerate(txt_file['linhas_do_arquivo']):
            if word.lower() in line.lower():
                found.append({'linha': index + 1}) \
                    if not show_line_content \
                    else found.append({'linha': index + 1, 'conteudo': line})
        if found:
            files_containing_word.append({
                'palavra': word,
                'arquivo': txt_file['nome_do_arquivo'],
                'ocorrencias': found
            })

    return files_containing_word


def search_by_word(word, instance):
    return exists_word(word, instance, True)
