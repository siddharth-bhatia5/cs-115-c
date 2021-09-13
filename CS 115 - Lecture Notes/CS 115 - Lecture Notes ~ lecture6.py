# CS 115-C
# Sid Bhatia
# Lecture #6 - Notes

# Python's functions have white-space defined with indentation

def date_to_string(num_date):
    """
    Convert a numerical date of the form YYYYMMDD as an 8-digit
    decimal number to text.

    e.g., 20200911 -> \'Sep 11, 2020\'
    """
    
    # In Python, there are no characters: they are just strings w/length 1
    # Python doesn't care if you use a single quote or double quote

    # \' is an escape-sequence for the single-quote (')

    # helper function
    def break_down_input():
        y = num_date // 10,000 #YYYYMMDD -> YYYY
        md = num_date % 10,000 #YYYYMMDD -> MMDD
        m = md // 100          #MMDD -> MM
        d = md % 100           #MMDD -> DD
        return y, m, d

    def month_as_string(m);
        # map MM of 1 to Jan, MM of 2, to Feb, ...
        
