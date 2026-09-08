# Invitación Digital: Bautizo & Cumpleaños de Aaron Sebastián Ortiz Alcantar

Diseño de alta gama inspirado en el **Reel floral con arco drapeado de terciopelo verde olivo, alcatraces blancos esculturales (calla lilies) y acentos heráldicos de Marvel**, con paleta **Negro Ónix, Beige Cantera y Verde Botánico**.

---

## 📅 Datos del Evento Configurados

* **Festejado**: Aaron Sebastián Ortiz Alcantar
* **Motivo**: Bautizo y Cumpleaños
* **Fecha**: Sábado, 3 de Octubre de 2026
* **Ceremonia Religiosa**:
  * Iglesia Nuestra Señora del Carmen (1:00 PM)
  * Avenida México Norte 117, Centro, 63000 Tepic, Nay. México
  * Enlaces integrados a Google Maps y Waze
* **Celebración & Recepción**:
  * Salón de Eventos La Lomita (3:30 PM)
  * Boulevard Tepic Xalisco #110, Col. La Curva del Guayabo, Tepic, Nayarit
  * Enlaces integrados a Google Maps y Waze
* **Mesa de Regalos**:
  * **Liverpool**: Evento número **60040338** ([Ver en Liverpool](https://mesaderegalos.liverpool.com.mx/milistaderegalos/60040338))
  * **Sugerencia de Sobre**: Tarjeta para transferencia con botón para copiar la cuenta CLABE en 1 clic.
* **Confirmación RSVP**:
  * Formulario que redacta automáticamente el mensaje estructurado con emojis y abre la conversación directa en WhatsApp.

---

## 🌿 Características de Diseño e Interactividad

1. **Arco Drapeado de Terciopelo Verde**:
   - Inspirado directamente en el montaje del Reel de Instagram, enmarcando la portada con textura, borlas y relieve dorado.
2. **Flores de Alcatraz (Calla Lilies) en Línea Fina**:
   - Ilustraciones botánicas en blanco puro y oro litúrgico entrelazadas con la estrella heroica.
3. **Piso con Textura de Mármol y Diamantes**:
   - Fondo sutil de cantera/mármol pulido que da profundidad y elegancia.
4. **Sobre & Sello Real de Cera**:
   - Sello con la "A" estilizada de los Vengadores y halo sagrado que desbloquea el audio en navegadores móviles.
5. **Música Ambiental y Partículas en Vivo**:
   - Canvas flotante con pétalos blancos de alcatraz, hojitas de eucalipto y destellos de oro.
6. **Muestrario de Dress Code**:
   - Círculos de color: Negro Ónix, Verde Olivo, Eucalipto, Beige Cantera y Marfil Alcatraz.

---

## 🚀 Despliegue en Vercel y Dominio Principal

Este proyecto ya cuenta con [`vercel.json`](./vercel.json).

Para conectarlo al proxy de `invitacionesdigitalesmty.com.mx`:
1. Sube este proyecto a tu GitHub: `JCCJN04/bautizo-aaron-sebastián` (o el nombre que elijas).
2. Conéctalo a Vercel.
3. Agrega la redirección en el `vercel.json` de tu proyecto principal (`invitacionesdigitales`):
   ```json
   {
     "source": "/bautizo-aaron-sebastian",
     "destination": "https://<nombre-en-vercel>.vercel.app/"
   },
   {
     "source": "/bautizo-aaron-sebastian/:path*",
     "destination": "https://<nombre-en-vercel>.vercel.app/:path*"
   }
   ```
