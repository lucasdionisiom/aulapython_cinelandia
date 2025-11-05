temperatura=float(input("Digite a temperatura:"))
if (temperatura<18):
      print(f"{temperatura} está frio")
elif(temperatura>=18 and temperatura <30):
      print(f"{temperatura} está agradável")
else:
      print(f"{temperatura} está calor")