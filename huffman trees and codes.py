from heapq import heappush, heappop, heapify
from collections import defaultdict

class Node:
    def __init__(self, frekuensi, karakter=None, kiri=None, kanan=None):
        self.frekuensi = frekuensi
        self.karakter = karakter
        self.kiri = kiri
        self.kanan = kanan

    def __lt__(self, other):
        return self.frekuensi < other.frekuensi

def bangun_pohon_huffman(data):
    frekuensi = defaultdict(int)
    for karakter in data:
        frekuensi[karakter] += 1

    heap = [Node(frekuensi[karakter], karakter) for karakter in frekuensi]
    heapify(heap)

    while len(heap) > 1:
        kiri = heappop(heap)
        kanan = heappop(heap)
        parent = Node(kiri.frekuensi + kanan.frekuensi, kiri=None, kanan=None)
        parent.kiri, parent.kanan = kiri, kanan
        heappush(heap, parent)

    return heappop(heap)

data = "program huffman trees sederhana dengan variabel bahasa indonesia"
root = bangun_pohon_huffman(data)

def traverse(node, kode=""):
    if node.karakter:
        print(f"{node.karakter}: {kode}")
    else:
        traverse(node.kiri, kode + "0")
        traverse(node.kanan, kode + "1")

traverse(root)
