
class Solution:
    def romanToInt(self, s: str) -> int:
        # values of each str variable stored as a dict 
        values = {
                    'I' : 1,
                    'V' : 5,
                    'X' : 10,
                    'L' : 50,
                    'C' : 100,
                    'D' : 500,
                    'M' : 1000}
        
        s = s.replace('IV', 'IIII') \
            .replace('IX','VIIII')  \
            .replace('XL','XXXX') \
            .replace('XC','LXXXX') \
            .replace('CD','CCCC') \
            .replace('CM','DCCCC')

        # use map to map the values of the dict and replace in strig or map in string 
        return sum(map(values.get , s))

    print(romanToInt("III"))