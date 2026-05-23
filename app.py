def calculadora_propinas():
    try:
        cuenta = float(input("¿Cuánto fue el total de la cuenta?: $"))
        porcentaje = int(input("¿Porcentaje de propina? (10, 15, 20): "))
        personas = int(input("¿Entre cuántas personas se va a dividir?: "))
        
        propina = cuenta * (porcentaje / 100)
        total_con_propina = cuenta + propina
        pago_por_persona = total_con_propina / personas
        
        print(f"\nTotal de propina: ${propina:.2f}")
        print(f"Total con propina: ${total_con_propina:.2f}")
        print(f"Cada persona paga: ${pago_por_persona:.2f}")
    except ValueError:
        print("Por favor, introduce números válidos.")

if __name__ == "__main__":
    calculadora_propinas()