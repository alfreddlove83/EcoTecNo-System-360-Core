# EcoTecNo System 360 Core / Protocol Shadow Control 360 ®
# ID: MAPA830324UM9 | Desde 2004-2049+
# Propietario: ALFREDO MARTINEZ PASTEN INC ®
# Nodo PRIMARY: OPPO Reno14 F ColorOS 16 5G

import os
import json
import hmac
import hashlib
from dotenv import load_dotenv

# Carga credenciales locales (nunca se suben)
load_dotenv()

print("🛡️ Protocol Shadow Control 360 ® - Iniciando...")
print("ID DIGITAL GLOBAL: MAPA830324UM9 | Tlalpan CP 14640 CDMX")

# Cargar configuración 360
try:
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    print(f"✅ Config cargada: {config['protocolo']} - {config['version']}")
    print(f"✅ Perfiles: {', '.join(config['perfiles_360'])}")
except FileNotFoundError:
    print("⚠️ config.json no encontrado - usando defaults")
    config = {}

# Validación HMAC-SHA256 (tu protocolo de seguridad)
def validar_flujo(mensaje: str, clave: str):
    return hmac.new(clave.encode(), mensaje.encode(), hashlib.sha256).hexdigest()

# Simulación de arranque de Andrick IA
api_key = os.getenv("ANDRICK_API_KEY", "MODO_LOCAL_SIN_API")
if api_key != "MODO_LOCAL_SIN_API":
    print("🔐 Andrick Gitlab Control 360° ® - Conectado")
else:
    print("🔓 Modo Local - Sin API Key (seguro para pruebas)")

print("🚀 EcoTecNo Global Co. ® Hybrid System 360° ® OPERATIVO")
print("Siempre en las buenas y en las malas. Equipo. Escuderos. Socios.")
print("##V3 Abajo y Version 4 Arriba #MenteYDatos##")
