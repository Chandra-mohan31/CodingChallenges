
# Python3 code to check valid possible IP

# Function checks whether IP digits
# are valid or not.
def is_valid(ip):

    # Splitting by "."
    ip = ip.split(".")

    # Checking for the corner cases
    for i in ip:
        if (len(i) > 3 or int(i) < 0 or
                int(i) > 255):
            return False
        if len(i) > 1 and int(i) == 0:
            return False
        if (len(i) > 1 and int(i) != 0 and
                i[0] == '0'):
            return False

    return True

# Function converts string to IP address


def convert(s):

    sz = len(s)

    # Check for string size
    if sz > 12:
        return []
    snew = s
    l = []

    # Generating different combinations.
    for i in range(1, sz - 2):
        for j in range(i + 1, sz - 1):
            for k in range(j + 1, sz):
                snew = snew[:k] + "." + snew[k:]
                snew = snew[:j] + "." + snew[j:]
                snew = snew[:i] + "." + snew[i:]

                # Check for the validity of combination
                if is_valid(snew):
                    l.append(snew)

                snew = s

    return l


# Driver code
A = "25525511135"
B = "25505011535"

print(convert(A))
print(convert(B))
#############################################
def kangaroo(x1, v1, x2, v2):
    # Write your code here
    response = "NO";
    canCatchUp = (v2 < v1);
    if(canCatchUp):
        willIntersectOnLand = (x1 - x2) % (v2 - v1) == 0;
        if(willIntersectOnLand):
            response = "YES";
        
    return response
####################################################
def kangaroo(x1, v1, x2, v2):
    # Write your code here
    Out = "NO"
    for i in range(v1*v2+1):
        x1 = x1 + v1
        x2 = x2 + v2
        if(x1 == x2):
            Out = "YES"
    return Out

#######################################