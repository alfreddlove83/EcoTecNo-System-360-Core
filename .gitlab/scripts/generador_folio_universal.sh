#!/bin/bash
# GENERADOR UNIVERSAL DE FOLIOS ECOTECNO 360° |%€✓
# Funciona desde cualquier terminal: Móvil, PC, Bot

FECHA=$(date +"%d%m%Y_%H:%M")
TERMINAL=$(uname -a | cut -d' ' -f2) # Detecta OPPO, iPhone, Chrome, etc.
TITULO=$1
FOLIO="RB360-Q4-2026-${FECHA}-${TITULO}"

echo "EcoTecNo // ${FECHA} // ${TITULO} // ${TERMINAL}" >> docs/trazabilidad/BITACORA_Q4_2026.md
echo "" >> docs/trazabilidad/BITACORA_Q4_2026.md
echo "### 📝 REGISTRO DE TRAZABILIDAD: ECOTECNO-${FOLIO}" >> docs/trazabilidad/BITACORA_Q4_2026.md
echo "* **Fecha/Hora:** ${FECHA} | **Terminal de Origen:** ${TERMINAL}" >> docs/trazabilidad/BITACORA_Q4_2026.md
echo "* **Estado Anterior:** [Auto-detectado por diff]" >> docs/trazabilidad/BITACORA_Q4_2026.md
echo "* **Modificación:** ${TITULO} desde ${TERMINAL}" >> docs/trazabilidad/BITACORA_Q4_2026.md
echo "" >> docs/trazabilidad/BITACORA_Q4_2026.md
echo "|%€✓ Colaboración Universal - @alfreddlove83 |%€✓" >> docs/trazabilidad/BITACORA_Q4_2026.md

git add docs/trazabilidad/BITACORA_Q4_2026.md
git commit -m "feat(trace): ${FOLIO} desde ${TERMINAL} |%€✓"
git push origin main