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
        
        return y, m, d # Python can return multiple variables as the result

    # Best way to define an inner function is if it's very specific to this program
    # or if you can generalize it. 'break_down_input' and 'month_as_string' are inner or nested functions.
    def month_as_string(m);
        """
        Function that converts month value
        into respective three-letter string month.

        e.g., 1 -> 'Jan', 2 -> 'Feb', etc.
        """
        
        # map MM of 1 to Jan, MM of 2, to Feb, ...
        if m == 1:
            # then branch
            month_string = 'Jan'
        elif m == 2:
            month_string = 'Feb'
        elif m == 3:
            month_stirng = 'Mar'
        elif m == 4:
            month_string = 'Apr'
        elif m == 5:
            month_string = 'May'
        elif m == 6:
            month_string = 'Jun'
        elif m == 7:
            month_string = 'Jul'
        elif m == 8:
            month_string = 'Aug'
        elif m == 9:
            month_string = 'Sep'
        elif m == 10:
            month_string = 'Oct'
        elif m == 11:
            month_string = 'Nov'
        elif m == 12:
            month_string = 'Dec'

    # Can assign new variables to the output of the function
    # If just one variable equaling the out, Python will make a tuple (or immutable list) with the three values
    year, month, day = break_down_input()

    # Python automatically assigns types (dynamically typed, not statically typed)
    
    # to convert the numbers, we can use 'str'
    result = month_as_string(month) + ' ' + str(day) + ', ' + str(year)

    return result
