from .file_management import txt_importer
import sys


def process(path_file, instance):
    result = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(txt_importer(path_file)),
        'linhas_do_arquivo': txt_importer(path_file)
    }
    for entry in instance._data:
        if entry['nome_do_arquivo'] == path_file:
            return None
    instance.enqueue(result)
    print(result)


def remove(instance):
    removed_element = instance.dequeue()
    if not removed_element:
        print("Não há elementos")
        return None
    print(f"Arquivo {removed_element['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        found_element = instance.search(position)
        print(found_element)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
