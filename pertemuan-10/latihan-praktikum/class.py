class StackList:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items)==0
    
    def push(self, url):
        self.items.append(url)
        
    def pop(self):
        if self.is_empty():
            return 'Riwayat Kosong.'
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
        
    def size(self):
        return len(self.items)
    
riwayatNavigasi = StackList()

riwayatNavigasi.push('Google')
riwayatNavigasi.push('Youtube')
riwayatNavigasi.push('Instagram')
riwayatNavigasi.push('Soliter')
riwayatNavigasi.push('Google Classroom')

print('Stack: ', riwayatNavigasi.items)
print('Pop: ', riwayatNavigasi.pop())
print('Peek: ', riwayatNavigasi.peek())
print('Stack setelah Pop: ', riwayatNavigasi.items)
print('isEmpty: ', riwayatNavigasi.is_empty())
print('Size: ', riwayatNavigasi.size())