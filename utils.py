class utils:
    def reversed(num: int) -> int:
        if not isinstance(num, int):
            raise TypeError("Input value must be of integer type")
        return int(str(num)[::-1])
    
    def formatter(num: int) -> (str, str):
        if not isinstance(num, int):
            raise TypeError("Input value must be of integer type")
        return (bin(num), oct(num))