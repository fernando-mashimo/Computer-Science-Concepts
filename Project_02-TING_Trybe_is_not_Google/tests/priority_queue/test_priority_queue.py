from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    queue = PriorityQueue()
    queue.enqueue({"qtd_linhas": 1, "nome_arquivo": "XYZ.txt"})
    assert len(queue) == 1
    assert queue.dequeue() == {"qtd_linhas": 1, "nome_arquivo": "XYZ.txt"}

    queue.enqueue({"qtd_linhas": 1, "nome_arquivo": "XYZ.txt"})
    queue.enqueue({"qtd_linhas": 99, "nome_arquivo": "XYZ.txt"})
    queue.enqueue({"qtd_linhas": 2, "nome_arquivo": "XYZ.txt"})
    assert queue.search(1) == {"qtd_linhas": 2, "nome_arquivo": "XYZ.txt"}

    with pytest.raises(IndexError):
        queue.search(3)
