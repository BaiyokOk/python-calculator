class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b #สลับ a กับ b ให้อยู่หน้าหลังตามลำดับ

    def multiply(self, a, b):
        result = 0
        for i in range(1, b+1): #เพิ่มจุดเริ่มต้นเป็น 1
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        result = 0
        while a >= b: #เปลี่ยนเครื่องหมาย > เป็น >=
            a = self.subtract(a, b)
            result += 1
        return result
    
    def modulo(self, a, b):
        while a >= b: #เปลี่ยนเครื่องหมาย <= เป็น >=
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))