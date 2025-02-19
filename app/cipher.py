class PlayfairCipher:
    def __init__(self, key):
        self.key = self._prepare_key(key)
        self.matrix = self._generate_matrix()

    def _prepare_key(self, key):
        # Convert to uppercase and remove non-letters
        key = ''.join(c.upper() for c in key if c.isalpha())
        # Replace J with I
        key = key.replace('J', 'I')
        
        # Remove duplicates while preserving order
        seen = set()
        key = ''.join(c for c in key if not (c in seen or seen.add(c)))
        
        # Add remaining alphabet
        alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        key += ''.join(c for c in alphabet if c not in key)
        
        return key

    def _generate_matrix(self):
        return [list(self.key[i:i+5]) for i in range(0, 25, 5)]

    def _find_position(self, char):
        for i in range(5):
            for j in range(5):
                if self.matrix[i][j] == char:
                    return i, j
        return None

    def _prepare_text(self, text):
        # Convert to uppercase and remove non-letters
        text = ''.join(c.upper() for c in text if c.isalpha())
        text = text.replace('J', 'I')
        
        # Split into digraphs and handle repeated letters
        result = []
        i = 0
        while i < len(text):
            if i == len(text) - 1:
                result.append(text[i] + 'X')
                break
            if text[i] == text[i + 1]:
                result.append(text[i] + 'X')
                i += 1
            else:
                result.append(text[i:i+2])
                i += 2
        
        return result

    def encrypt(self, plaintext):
        digraphs = self._prepare_text(plaintext)
        result = []
        
        for pair in digraphs:
            row1, col1 = self._find_position(pair[0])
            row2, col2 = self._find_position(pair[1])
            
            if row1 == row2:  # Same row
                result.append(self.matrix[row1][(col1 + 1) % 5] + 
                            self.matrix[row2][(col2 + 1) % 5])
            elif col1 == col2:  # Same column
                result.append(self.matrix[(row1 + 1) % 5][col1] + 
                            self.matrix[(row2 + 1) % 5][col2])
            else:  # Rectangle case
                result.append(self.matrix[row1][col2] + 
                            self.matrix[row2][col1])
        
        return ''.join(result)

    def decrypt(self, ciphertext):
        digraphs = self._prepare_text(ciphertext)
        result = []
        
        for pair in digraphs:
            row1, col1 = self._find_position(pair[0])
            row2, col2 = self._find_position(pair[1])
            
            if row1 == row2:  # Same row
                result.append(self.matrix[row1][(col1 - 1) % 5] + 
                            self.matrix[row2][(col2 - 1) % 5])
            elif col1 == col2:  # Same column
                result.append(self.matrix[(row1 - 1) % 5][col1] + 
                            self.matrix[(row2 - 1) % 5][col2])
            else:  # Rectangle case
                result.append(self.matrix[row1][col2] + 
                            self.matrix[row2][col1])
        
        return ''.join(result) 