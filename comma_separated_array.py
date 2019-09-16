#comma_separated_array
#LIST   TUPLE   SET

ARR = input("ENTER THE ARRAY ").split(",") #GET INPUT AS LIST
print("LIST ", ARR)
tpl = tuple(ARR)        #MOVING THE LIST TO TUPLE
print("TUPLE ", tpl)    #NOTE: TUPLE CANT BE UPDATED OR MODIFIED
st = set(ARR)           #SET WILL DELETE THE REPEATED ELEMENTS
print("SET ", st)