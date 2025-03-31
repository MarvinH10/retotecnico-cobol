import csv, argparse

def procesar_csv(archivo):
    balance, trans_max, conteo = 0, {"id": None, "monto": float("-inf")}, {"Crédito": 0, "Débito": 0}
    op = {"Crédito": 1, "Débito": -1}
    with open(archivo, newline="", encoding="UTF-8") as f:
        for row in csv.DictReader(f):
            tipo, monto, tid = row["tipo"].strip(), float(row["monto"].strip()), row["id"].strip()
            balance += monto * op.get(tipo, 0)
            conteo[tipo] += 1
            if monto > trans_max["monto"]:
                trans_max = {"id": tid, "monto": monto}
    return balance, trans_max, conteo

def mostrar_reporte(balance, trans_max, conteo):
    print("Reporte de Transacciones")
    print("-" * 45)
    print(f"Balance Final: {balance:.2f}")
    print(f"Transacción de Mayor Monto: ID {trans_max['id']} - {trans_max['monto']:.2f}")
    print(f"Conteo de Transacciones: Crédito: {conteo['Crédito']} Débito: {conteo['Débito']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Procesa un CSV de transacciones bancarias y genera un reporte.")
    parser.add_argument("archivo", help="Ruta del CSV a procesar")
    args = parser.parse_args()
    mostrar_reporte(*procesar_csv(args.archivo))
