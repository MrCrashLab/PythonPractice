import struct


def create_structure_b(byte):
    data_b = dict()
    address_c = [struct.unpack('=I', byte[16 + 4 * j:20 + 4 * j])[0] for j in range(4)]
    tmp_c = [struct.unpack('HH', byte[address_c[i] + 12:address_c[i] + 16]) for i in range(4)]
    data_b['B1'] = [
        {'C1': [struct.unpack('=H', byte[address_c[i] + 2 * j:address_c[i] + 2 * (j + 1)])[0] for j in range(6)],
         'C2': list(struct.unpack('=' + 'b' * tmp_c[i][0], byte[tmp_c[i][1]:tmp_c[i][1] + 1 * tmp_c[i][0]]))}
        for i in range(4)]
    data_b['B2'] = struct.unpack('=I', byte[32:36])[0]
    data_b['B3'] = struct.unpack('=i', byte[36:40])[0]
    data_b['B4'] = struct.unpack('=q', byte[40:48])[0]
    return data_b


def create_structure_d(byte):
    data_d = dict()
    address_d = struct.unpack('=H', byte[72:74])[0]
    data_d['D1'] = struct.unpack('=q', byte[address_d:address_d + 8])[0]
    data_d['D2'] = struct.unpack('=I', byte[address_d + 8:address_d + 12])[0]
    tmp_d = struct.unpack('IH', byte[address_d + 12:address_d + 18])
    data_d['D3'] = list(struct.unpack('=' + 'h' * tmp_d[0], byte[tmp_d[1]:tmp_d[1] + 2 * tmp_d[0]]))
    data_d['D4'] = struct.unpack('=i', byte[address_d + 18:address_d + 24])[0]
    return data_d


def f31(byte):
    data = dict()
    data['A1'] = struct.unpack('=b', byte[4:5])[0]
    data['A2'] = struct.unpack('=d', byte[5:13])[0]
    data['A3'] = struct.unpack('=H', byte[13:15])[0]
    data['A4'] = struct.unpack('=B', byte[15:16])[0]
    data['A5'] = create_structure_b(byte)
    data['A6'] = list(struct.unpack('=6f', byte[48:72]))
    data['A7'] = create_structure_d(byte)
    return data


class C32:
    a = 'A'
    b = 'B'
    c = 'C'
    d = 'D'
    e = 'E'
    f = 'F'
    g = 'G'
    h = 'H'
    state = a

    def fade(self):
        if self.state == self.a:
            self.state = self.b
            return 0
        elif self.state == self.d:
            self.state = self.f
            return 6
        elif self.state == self.g:
            self.state = self.g
            return 11
        else:
            return None

    def zoom(self):
        if self.state == self.a:
            self.state = self.f
            return 1
        elif self.state == self.b:
            self.state = self.c
            return 2
        elif self.state == self.c:
            self.state = self.d
            return 3
        elif self.state == self.d:
            self.state = self.e
            return 4
        else:
            return None

    def type(self):
        if self.state == self.e:
            self.state = self.f
            return 7
        elif self.state == self.d:
            self.state = self.h
            return 5
        elif self.state == self.f:
            self.state = self.c
            return 9
        elif self.state == self.g:
            self.state = self.h
            return 10
        else:
            return None

    def skew(self):
        if self.state == self.f:
            self.state = self.g
            return 8
        else:
            return None


