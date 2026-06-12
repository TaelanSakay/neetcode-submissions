class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        Sclean = sorted(s)
        Tclean = sorted(t)

        if Sclean == Tclean:
            return True
        return False