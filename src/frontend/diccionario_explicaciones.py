"""
frontend/diccionario_explicaciones.py
====================================================================
Textos de ayuda para la interfaz (Tooltips y Expanders).
====================================================================
"""

TOOLTIPS = {
    # Sidebar
    "umbral_alerta": "Define el nivel mínimo del Pain Index (0-10) para disparar alertas visuales y registrar dolor persistente en el historial.",
    "intervalo_reproduccion": "Tiempo de espera antes de que el sistema avance automáticamente a la siguiente época de datos.",
    
    # Resumen
    "peso_fusion": "Ajusta qué tanta importancia se le da a la señal cerebral (EEG) frente a la corporal (Biomarcadores) al calcular el Pain Index.",
    "pain_index": "Índice ponderado del 0 al 10 que estima la severidad del dolor cruzando los modelos de Inteligencia Artificial.",
    
    # Cerebro (XAI)
    "electrodo_dom": "Electrodo con mayor peso matemático en la decisión de la red neuronal. Indica la región del cuero cabelludo más activa para esta predicción.",
    "shap_eeg": "Método de atribución: Evalúa qué electrodos aportaron más 'evidencia' a favor del diagnóstico de dolor comparando la señal real contra un ruido base.",
    "gradcam": "Mapa de calor interno: Analiza las capas de la red neuronal para identificar en qué milisegundo exacto ocurrió el pico de procesamiento de dolor.",
    "lime_eeg": "Oclusión temporal: El sistema 'apaga' partes de la onda secuencialmente. Los picos en este gráfico indican qué fragmentos de la onda son indispensables para que la IA detecte el dolor.",
    
    # Cuerpo
    "shap_cuerpo": "Impacto Global: Muestra qué biomarcadores son, en general, los más determinantes para que el modelo XGBoost tome decisiones.",
    "lime_cuerpo": "Impacto Local: Muestra por qué el modelo tomó esta decisión *específicamente para este paciente* en este instante, simulando pequeñas variaciones en sus signos vitales.",
    
    # Historial
    "racha_dolor": "El sistema audita si el dolor es un pico aislado o si se mantiene constante por encima del umbral definido."
}
