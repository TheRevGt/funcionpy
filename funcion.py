def ecuacion():
	frutas=int(input("ingrese el precio de las frutas: "))
	verduras=int(input("ingrese el precio de las verduras: "))
	granos=int(input("ingrese el precio de las granos: "))
	pre=int(input("Cuanto es el presupuesto de compra: "))
	x=frutas+verduras+granos
	if x <= pre:
		y=5+2+3 #Descuento
		p=x-y #Restar descuentos al total
		v=pre-p #Vuelto del cliente
		print("El resultado de la suma es: ",x, "\nTodoal de descuento: ",y, "\nPagar:", p, "\nVuelto:", v)
	else:
		print("No puede gastar más de su presupuesto")
	return "Finalizado"
print(ecuacion())
