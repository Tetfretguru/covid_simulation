import paises as p

""" Limpiar código """
daily_cases = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,6,6,29,50,79,79,110,110,158,162,189,217,238,238,303,303,294,296,286,284,296,302,296,286,267,257,257,260,273,274,227,224,212,207,207,210,209,212,207,200,200,182,182,212,216,219,216,209,196,195,196,193,185,170,175,170,171,171,169,166,155,158,160,156,150,148,139,138,135,130,126,129,136,129,131,135,114,117,116,113,112,107,100,90,96,92,84,69,66,52,44,40,37,33,24,15,12,15,19,37,42,45,61,63,75,80,84,83,85,90,91,87,87,79,73,71,74,70,70,60,60,55,61,69,78,88,90,99,104,134,149,167,186,193,210,216,225,235,230,235]  
active_cases = daily_cases 
pais = p.Country('Uruguay', 'South America', 3400000, active_cases)
print(pais)